from flask import Blueprint, request
from configuracion import mysql
import MySQLdb
from flask_cors import cross_origin
from helpers import *
import json

actualizar = Blueprint('actualizar',__name__)

@actualizar.route('/modificaCliente/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_cliente(id):
    nombre = request.json.get('nombre')
    logo = request.json.get('logo')
    direccion = request.json.get('direccion')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')
    giro = request.json.get('giro')
    producto = request.json.get('producto')

    try:
        sql = 'update cliente set nombre=%s,logo=%s,direccion=%s, telefono=%s,correo=%s, giro=%s,producto=%s where idCliente=%s'
        cur = mysql.connection.cursor()
        cur.execute(sql,(nombre,logo,direccion,telefono,correo,giro,producto,id))
        mysql.connection.commit()
        return 'ok',200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@actualizar.route('/modificarConf/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_conf(id):
    nombre = request.json.get('nombre')
    colorPrim = request.json.get('colorPrim')
    colorSec = request.json.get('colorSec')
    colorTer = request.json.get('colorTer')
    colorTxtBtn = request.json.get('colorTxtBtn')
    colorBtn = request.json.get('colorBtn')
    tipografiaTitulos = request.json.get('tipografiaTitulos')
    tipografiaContent = request.json.get('tipografiaContent')
    orden = request.json.get('orden')
    
    try:
        sql = 'update configuracion set nombreConf=%s,colorPrim=%s,colorSec=%s,colorTer=%s,colorTxtBtn=%s,colorBtn=%s,orden=%s,idTipografia=%s,idTipografiaContent=%s where idConf=%s'
        cur = mysql.connection.cursor();
        cur.execute(sql,(nombre,colorPrim,colorSec,colorTer,colorTxtBtn,colorBtn,orden,tipografiaTitulos,tipografiaContent,id))
        mysql.connection.commit()
        return 'ok',200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@actualizar.route('/modificarUsuario/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_usuario(id):
    correo = request.json.get('correo')
    nombre = request.json.get('nombre')
    contrasenia = request.json.get('contrasenia')
    
    try:
        sql = 'update usuarios set usuario=%s,contrasenia=%s,correo=%s where idUsuario=%s'
        cur = mysql.connection.cursor();
        cur.execute(sql,(nombre, contrasenia, correo, id))
        mysql.connection.commit()
        return 'ok',200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@actualizar.route('/modificaDisenio/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_disenio(id):
    nombre = request.json.get('nombre')
    idHeader = request.json.get('header')
    idSlide = request.json.get('slide')
    idAbout = request.json.get('about')
    idAction = request.json.get('accion')
    idFormulario = request.json.get('formulario')
    idTestimonio = request.json.get('testimonios')
    idBeneficio = request.json.get('beneficios')
    idFooter = request.json.get('footer')
    idConf = request.json.get('configuracion')
    
    try:
        sql = 'update disenio set nombre=%s,idHeader=%s,idSlide=%s,idAbout=%s,idTestimonio=%s,idBeneficios=%s,idFormularios=%s,idFooter=%s,idConf=%s,idAccion=%s where idDisenio=%s'
        cur = mysql.connection.cursor();
        cur.execute(sql,(nombre,idHeader,idSlide,idAbout,idTestimonio,idBeneficio,idFormulario,idFooter,idConf,idAction,id))
        mysql.connection.commit()
        return 'ok',200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@actualizar.route('/modificaCampania/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_campania(id):
    nombre = request.json.get('nombre')
    fechaIni = request.json.get('fechaIni')
    fechaFin = request.json.get('fechaFin')
    
    try:
        sql = 'update campania set nombre=%s, fechaIni=%s, fechaFin=%s where idCampania=%s'
        cur = mysql.connection.cursor();
        cur.execute(sql,(nombre,fechaIni,fechaFin,id))
        mysql.connection.commit()
        return 'ok',200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@actualizar.route('/modificaContenido/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenidoHeader(id):
    try:
        cur = mysql.connection.cursor()

        contacto = request.json.get('contacto')
        contenidoHeader = request.json.get('contentHeader')
        contenidoSlide = request.json.get('contentSlide')
        contenidoAbout = request.json.get('contentAbout')
        contenidoAction = request.json.get('contentAction')
        contenidoBeneficios = request.json.get('contentBeneficios')
        contenidoFooter = request.json.get('contentFooter')
        contenidoTestimonios = request.json.get('contentTestimonios')
        contenidoFormulario = request.json.get('contentFormulario')
        contenidoPixel = request.json.get('contentPixel')
        contenidoStyle = request.json.get('contentStyle')

        contenido={
            'contacto':contacto,
            'contentHeader':contenidoHeader,
            'contentSlide':contenidoSlide,
            'contentAbout':contenidoAbout,
            'contentAction':contenidoAction,
            'contentBeneficios':contenidoBeneficios,
            'contentFooter':contenidoFooter,
            'contentTestimonios':contenidoTestimonios,
            'contentForm':contenidoFormulario,
            'contentPixel':contenidoPixel,
            'contentStyle':contenidoStyle
        }

        sql = 'update contenido set contenido=%s where idContent=%s'
        cur.execute(sql,(json.dumps(contenido),id))
        mysql.connection.commit()
        return 'ok',200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@actualizar.route('/modStatusCliente/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_status_cliente(id):
    status = request.json.get('status')
    
    try:

        cur = mysql.connection.cursor();

        cur.execute("update campania set status=%s where idCliente=%s",(status,id))
        mysql.connection.commit()
        
        cur.execute('select campania.idCampania from campania, cliente where cliente.idCliente = campania.idCliente and cliente.idCliente = {0}'.format(id));

        idCampanias = cur.fetchall()

        for idCampania in idCampanias:
            cur.execute('update disenio set status=%s where idCampania=%s',(status,idCampania))
            mysql.connection.commit()

        return 'ok',200

    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@actualizar.route('/modStatusCampania/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_status_campania(id):
    status = request.json.get('status')
    
    try:
        sql = "update campania set status=%s where idCampania=%s"
        cur = mysql.connection.cursor()
        cur.execute(sql,(status,id))
        mysql.connection.commit()

        cur.execute('update disenio set status=%s where idCampania=%s',(status,id))
        mysql.connection.commit()

        return 'ok',200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()

@actualizar.route('/modStatusDisenio/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_status_disenio(id):
    status = request.json.get('status')
    
    try:
        sql = "update disenio set status=%s where idDisenio=%s"
        cur = mysql.connection.cursor()
        cur.execute(sql,(status,id))
        mysql.connection.commit()
        return 'ok',200
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return 'Error',400
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return 'Error',400
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    finally:
        cur.close()