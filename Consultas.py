
from flask import Blueprint,request, jsonify
from configuracion import mysql
from flask_jwt_extended import create_access_token
import json
import MySQLdb
from helpers import *

consultas = Blueprint('consultas',__name__)

@consultas.route('/clientes', methods=['GET'])
def get_clientes():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from cliente')
        clientes = eliminarVacios(Convert(str(cur.fetchall())))
        return json.dumps(clientes), 200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/cliente/<id>', methods=['GET'])
def get_cliente(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from cliente where idCliente = {0}'.format(id))
        cliente = cur.fetchone()
        return json.dumps(cliente),200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/configuraciones', methods=['GET'])
def get_configuraciones():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select configuracion.idConf configuracion.nombreConf, configuracion.colorPrim,configuracion.colorSec,configuracion.orden,tipografia.tipografiaPrim,tipografia.tipografiaSec from configuracion, tipografia where configuracion.idTipografia=tipografia.idTipografia')
        configuraciones = eliminarVacios(Convert(str(cur.fetchall())))
        return json.dumps(configuraciones), 200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/configuracion/<id>', methods=['GET'])
def get_configuracion(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select configuracion.nombreConf, configuracion.colorPrim, configuracion.colorSec,configuracion.orden,tipografia.tipografiaPrim,tipografia.tipografiaSec from configuracion, tipografias where idConf = %s and configuracion.idTipografia = tipografia.idTipografia',[id])
        configuracion = cur.fetchone()
        return json.dumps(configuracion), 200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/campania', methods=['GET'])
def get_campania():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select campania.idCampania, campania.nombre,campania.fechaIni,campania.fechaFin, cliente.nombre from cliente, campania where campania.idCliente=cliente.idCliente')
        campanias = eliminarVacios(Convert(str(cur.fetchall())))

        cur.execute('select disenio.idDisenio, disenio.nombre from disenio, campania where disenio.idCampania=campania.idCampania')
        disenios = eliminarVacios(Convert(str(cur.fetchall())))
        
        datosCampanias = {
            'campanias':campanias,
            'disenios':disenios
        }

        return json.dumps(datosCampanias),200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/diseños', methods=['GET'])
def get_disenios():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select disenio.idDisenio, disenio.nombre,configuracion.nombreConf,cliente.nombre from disenio, configuracion,cliente where disenio.idCliente=cliente.idCliente and disenio.idConf=configuracion.idConf')
        disenios = eliminarVacios(Convert(str(cur.fetchall())))
        return json.dumps(disenios),200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()


@consultas.route('/diseño/<id>', methods=['GET'])
def get_disenio(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from disenio where idDisenio={0}'.format(id))
        disenio = cur.fetchone()
        return json.dumps(disenio),200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/tipografias',methods=['GET'])
def get_tipografias():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from tipografia')
        tipografias = cur.fetchall()
        return json.dumps(tipografias),200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/usuarios',methods=['GET'])
def get_usuarios():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from usuarios')
        tipografias = cur.fetchall()
        return json.dumps(tipografias),200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/usuario/<id>',methods=['GET'])
def get_usuario(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from usuarios where idUsuario = %s',[id])
        tipografias = cur.fetchone()
        return json.dumps(tipografias),200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/seleccionSecciones')
def get_secciones():
    try:
        cur = mysql.connection.cursor();

        cur.execute('select idHeader, header from headers')
        header = eliminarVacios(Convert(str(cur.fetchall())))

        cur.execute('select idSlide, slide from slides')
        slide = eliminarVacios(Convert(str(cur.fetchall())))

        cur.execute('select idAbout, about from abouts')
        about = eliminarVacios(Convert(str(cur.fetchall())))

        cur.execute('select idTestimonio, testimonio from testimonios')
        testimonio = eliminarVacios(Convert(str(cur.fetchall())))

        cur.execute('select idBeneficios, beneficios from beneficios')
        beneficios = eliminarVacios(Convert(str(cur.fetchall())))
        
        cur.execute('select idFormulario, formulario from formularios')
        formulario = eliminarVacios(Convert(str(cur.fetchall())))

        cur.execute('select idFooter, footer from footers')
        footer = eliminarVacios(Convert(str(cur.fetchall())))

        cur.execute('select idCampania, nombre from campania')
        campanias = eliminarVacios(Convert(str(cur.fetchall())))

        cur.execute('select idConf, nombreConf from configuracion')
        configuracion = eliminarVacios(Convert(str(cur.fetchall())))

        res = {
            'header':header,
            'slide':slide, 
            'about':about, 
            'testimonio':testimonio, 
            'beneficios':beneficios, 
            'formulario':formulario,
            'footer':footer, 
            'campanias':campanias, 
            'configuracion':configuracion
            }

        return json.dumps(res), 200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/token',methods=['POST'])
def get_token():
    usuario = request.json.get('usuario')
    contrasenia = request.json.get('contrasenia')

    try:
        cur = mysql.connection.cursor();
        cur.execute('select usuario, contrasenia from usuarios where usuario = %s and contrasenia = %s',(usuario,contrasenia))
        user = cur.fetchone()

        if user[0] != usuario and user[1] != contrasenia:
            return jsonify({"msg":"Usuario o contraseña incorrectos"})
        
        access_token = create_access_token(identity=usuario)
        return jsonify(access_token=access_token), 200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@consultas.route('/tokenSuperUsuario',methods=['POST'])
def get_token_superusuario():
    usuario = request.json.get('usuario')
    contrasenia = request.json.get('contrasenia')

    try:
        cur = mysql.connection.cursor();
        cur.execute('select superUsuario from usuarios where usuario = %s and contrasenia = %s',(usuario,contrasenia))
        user = cur.fetchone()

        if user[0] != 1:
            return jsonify({"msg":"No eres un super usuario"}), 403
        
        access_token = create_access_token(identity=usuario)
        return jsonify(access_token=access_token), 200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error'
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error'
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()