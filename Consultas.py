
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
        clientes = cur.fetchall()
        data=[]
        for cliente in clientes:
            dat = {
                'idCliente':cliente[0],
                'nombre':cliente[1],
                'logo':cliente[2],
                'direccion':cliente[3],
                'telefono':cliente[4],
                'correo':cliente[5],
                'giro':cliente[6],
                'producto':cliente[7],
                'user':cliente[8]
            }
            data.append(dat)

        return json.dumps(data), 200
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

@consultas.route('/cliente/<id>', methods=['GET'])
def get_cliente(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from cliente where idCliente = {0}'.format(id))
        cliente = cur.fetchone()
       
        data = {
            'idCliente':cliente[0],
            'nombre':cliente[1],
            'logo':cliente[2],
            'direccion':cliente[3],
            'telefono':cliente[4],
            'correo':cliente[5],
            'giro':cliente[6],
            'producto':cliente[7],
            'status':cliente[8]
        }

        return json.dumps(data), 200
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

@consultas.route('/campania/<id>', methods=['GET'])
def get_campania(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from campania where idcampania = {0}'.format(id))
        campania = cur.fetchone()
        data = {
            'idCampania':campania[0],
            'nombre':campania[1],
            'fechaIni':campania[2].strftime("%Y-%m-%d"),
            'fechaFin':campania[3].strftime("%Y-%m-%d"),
            'idCliente':campania[4],
            'status':campania[5]
        }
        return json.dumps(data),200
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

@consultas.route('/configuraciones', methods=['GET'])
def get_configuraciones():
    try:
        cur = mysql.connection.cursor()
        sql ="select configuracion.idConf,configuracion.nombreConf,configuracion.colorPrim,configuracion.colorSec,configuracion.colorTer,configuracion.colorBtn,configuracion.colorTxtBtn,configuracion.orden,(select tipografia from tipografias where configuracion.idTipografia=tipografias.idTipografia) as TipografiaTitulos,(select tipografia from tipografias where configuracion.idTipografiaContent=tipografias.idTipografia) as TipografiaContent from configuracion"

        cur.execute(sql)
        configuraciones = cur.fetchall()

        data = []

        for conf in configuraciones:
            dat={
                'idConf':conf[0],
                'nombreConf':conf[1],
                'colorPrim':conf[2],
                'colorSec':conf[3],
                'colorTer':conf[4],
                'colorBtn':conf[5],
                'colorTxtBtn':conf[6],
                'orden':conf[7],
                'tipografiaPrim':conf[8],
                'tipografiaSec':conf[9]
            }

            data.append(dat)

        return json.dumps(data), 200
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

@consultas.route('/configuracion/<id>', methods=['GET'])
def get_configuracion(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from configuracion where idConf = %s',[id])
        configuracion = cur.fetchone()

        dat={
                'idConf':configuracion[0],
                'nombre':configuracion[1],
                'colorPrim':configuracion[2],
                'colorSec':configuracion[3],
                'colorTer':configuracion[4],
                'colorBtn':configuracion[5],
                'colorTxtBtn':configuracion[6],
                'orden':json.loads(configuracion[7]),
                'tipografiaTitulos':configuracion[8],
                'tipografiaContent':configuracion[9]
            }

        return json.dumps(dat), 200
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

@consultas.route('/ordenConf/<id>', methods=['GET'])
def get_orden_conf(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select configuracion.orden from configuracion,disenio where configuracion.idConf=disenio.idConf and disenio.idDisenio={0}'.format(id))
        configuracion = cur.fetchone()

        dat={
                'idConf':configuracion[0],
                'nombre':configuracion[1],
                'colorPrim':configuracion[2],
                'colorSec':configuracion[3],
                'colorTer':configuracion[4],
                'colorBtn':configuracion[5],
                'colorTxtBtn':configuracion[6],
                'orden':configuracion[7],
                'tipografiaTitulos':configuracion[8],
                'tipografiaContent':configuracion[9]
            }

        return json.dumps(dat), 200
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

@consultas.route('/campanias', methods=['GET'])
def get_campanias():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select campania.idcampania,campania.nombre,campania.fechaIni,campania.fechaFin,cliente.nombre,campania.status,campania.user from campania,cliente where campania.idCliente=cliente.idCliente')
        campanias = cur.fetchall()
        data=[]
        for campania in campanias:
            dat = {
                'idCampania':campania[0],
                'nombre':campania[1],
                'fechaIni':campania[2].strftime("%Y-%m-%d"),
                'fechaFin':campania[3].strftime("%Y-%m-%d"),
                'cliente':campania[4],
                'status':campania[5],
                'user':campania[6]
            }
            data.append(dat)

        return json.dumps(data),200
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

@consultas.route('/diseniosCampania/<id>', methods=['GET'])
def get_disenios_campania(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select disenio.idDisenio, disenio.nombre,configuracion.nombreConf,campania.nombre, disenio.status,cliente.giro from disenio, configuracion,campania,cliente where disenio.idcampania=campania.idCampania and disenio.idConf=configuracion.idConf and campania.idCampania={0} and cliente.idCliente=campania.idCliente'.format(id))
        disenios = cur.fetchall()

        dataDisenio = []

        for disenio in disenios:
            dat = {
                'idDisenio':disenio[0],
                'nombreDisenio':disenio[1],
                'nombreConf':disenio[2],
                'nombreCampania':disenio[3],
                'status':disenio[4],
                'giro':disenio[5]
            }
            dataDisenio.append(dat)

        cur.execute('select contenido.idDisenio from contenido,campania,disenio where disenio.idDisenio=contenido.idDisenio and disenio.idCampania=campania.idCampania and campania.idCampania={0}'.format(id))
        content = cur.fetchall()

        dataContent = []
        for cont in content:
            dat = {
                'idContent':cont[0]
            }

            dataContent.append(dat);

        datos = {
            'data':dataDisenio,
            'content':dataContent
        }

        return json.dumps(datos),200
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


@consultas.route('/disenio/<id>', methods=['GET'])
def get_disenio(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from disenio where idDisenio={0}'.format(id))
        disenio = cur.fetchone()

        data = {
            'idDisenio': disenio[0],
            'nombre':disenio[1],
            'header':disenio[2],
            'slide':disenio[3],
            'about':disenio[4],
            'testimonios':disenio[5],
            'beneficios':disenio[6],
            'formulario':disenio[7],
            'footer':disenio[8],
            'configuracion':disenio[9],
            'idCampania':disenio[10],
            'accion':disenio[11]
        }

        return json.dumps(data),200
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

@consultas.route('/tipografias',methods=['GET'])
def get_tipografias():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from tipografias')
        tipografiaTitulos = cur.fetchall()
        dataTipografias = []
        for tipo in tipografiaTitulos:
            dat={
                'idTipografia': tipo[0],
                'tipografia': tipo[1]
            }
            dataTipografias.append(dat)

        return json.dumps(dataTipografias),200
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

@consultas.route('/usuarios',methods=['GET'])
def get_usuarios():
    try:
        cur = mysql.connection.cursor();
        cur.execute('select idUsuario,correo,usuario,superUsuario from usuarios');
        usuarios = cur.fetchall()

        data=[]
        for usuario in usuarios:
            dat = {
                'idUsuario':usuario[0],
                'correo':usuario[1],
                'nombre':usuario[2],
                'superUsuario':usuario[3]
            }
            data.append(dat)

        return json.dumps(data),200
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

@consultas.route('/usuario/<id>',methods=['GET'])
def get_usuario(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from usuarios where idUsuario = %s',[id])
        usuario = cur.fetchone()
        
        data = {
            'idUsuario':usuario[0],
            'correo':usuario[1],
            'nombre':usuario[2],
            'contrasenia':usuario[3]
        }

        return json.dumps(data),200
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

@consultas.route('/seleccionSecciones',methods=['GET'])
def get_secciones():
    try:
        cur = mysql.connection.cursor();

        cur.execute('select idHeader, header from headers')
        header = cur.fetchall()

        dataHeader=[]
        for head in header:
            dat = {
                'idHeader':head[0],
                'header':head[1]
            }
            dataHeader.append(dat)

        cur.execute('select idSlide, slide from slides')
        slide = cur.fetchall()

        dataslide=[]
        for sli in slide:
            dat = {
                'idSlide':sli[0],
                'slide':sli[1]
            }
            dataslide.append(dat)

        cur.execute('select idAbout, about from abouts')
        about = cur.fetchall()

        dataAbout=[]
        for abo in about:
            dat = {
                'idAbout':abo[0],
                'about':abo[1]
            }
            dataAbout.append(dat)

        cur.execute('select idTestimonio, testimonio from testimonios')
        testimonio = cur.fetchall()

        dataTestimonio=[]
        for testi in testimonio:
            dat = {
                'idTestimonio':testi[0],
                'testimonio':testi[1]
            }
            dataTestimonio.append(dat)

        cur.execute('select idBeneficios, beneficios from beneficios')
        beneficios = cur.fetchall()

        dataBeneficios=[]
        for benef in beneficios:
            dat = {
                'idBeneficios':benef[0],
                'beneficios':benef[1]
            }
            dataBeneficios.append(dat)
        
        cur.execute('select idFormulario, formulario from formularios')
        formulario = cur.fetchall()

        dataFormulario=[]
        for formu in formulario:
            dat = {
                'idFormulario':formu[0],
                'formulario':formu[1]
            }
            dataFormulario.append(dat)

        cur.execute('select idFooter, footer from footers')
        footer = cur.fetchall()

        dataFooter=[]
        for foot in footer:
            dat = {
                'idFooter':foot[0],
                'footer':foot[1]
            }
            dataFooter.append(dat)

        cur.execute('select idConf, nombreConf,orden from configuracion')
        configuracion = cur.fetchall()

        dataNombreConf=[]
        for configur in configuracion:
            dat = {
                'idConf':configur[0],
                'configuracion':configur[1],
                'orden':json.loads(configur[2])
            }
            dataNombreConf.append(dat)

        cur.execute('select idAccion, accion from acciones')
        accion = cur.fetchall()

        dataAccion=[]
        for acci in accion:
            dat = {
                'idAccion':acci[0],
                'accion':acci[1]
            }
            dataAccion.append(dat)

        res = {
            'header':dataHeader,
            'slide':dataslide, 
            'about':dataAbout, 
            'testimonio':dataTestimonio, 
            'beneficios':dataBeneficios, 
            'formulario':dataFormulario,
            'accion':dataAccion,
            'footer':dataFooter, 
            'configuracion':dataNombreConf
            }

        return json.dumps(res), 200
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

@consultas.route('/token',methods=['POST'])
def get_token():
    usuario = request.json.get('usuario')
    contrasenia = request.json.get('contrasenia')

    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from usuarios where usuario = %s and contrasenia = %s',(usuario,contrasenia))
        user = cur.fetchone()  
        
        if user != None:

            dataUser = {
                'idUsuario':user[0],
                'correo':user[1],
                'usuario':user[2],
                'superUsuario':user[4]
            }

            if user[2] != usuario and user[3] != contrasenia:
                return jsonify({"msg":"usuario o contraseña incorrectos"}),403
            
            elif user[2] == usuario and user[3] == contrasenia and user[4]==1:
                access_token = create_access_token(identity=usuario)
                return jsonify({
                    'accessToken':access_token,
                    'superUser':True,
                    'user':dataUser
                    }),200
            else:
                access_token = create_access_token(identity=usuario)
                return jsonify({
                    'accessToken':access_token,
                    'superUser':False,
                    "user":dataUser
                    }), 200
        else:
            return jsonify({'msg':'El usuario no existe'}),403
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

@consultas.route('/heatmap/<idDisenio>',methods=['GET'])
def get_heatmap(idDisenio):

    try:
        cur = mysql.connection.cursor();
        cur.execute('select * from disenio, configuracion where configuracion.idConf=disenio.idConf and disenio.idDisenio=%s',[idDisenio])
        heatmap = cur.fetchone()  
        
        if heatmap != None:

            dataDisenio = {
                'idDisenio':heatmap[0],
                'nombreDisenio':heatmap[1],
                'idHeader':heatmap[2],
                'idSlide':heatmap[3],
                'idAbout':heatmap[4],
                'idTestimonio':heatmap[5],
                'idBeneficios':heatmap[6],
                'idFormularios':heatmap[7],
                'idFooter':heatmap[8],
                'idConf':heatmap[9],
                'idCampania':heatmap[10],
                'idAccion':heatmap[11]
            }

            dataConf = {
                'idConf':heatmap[13],
                'nombreConf':heatmap[14],
                'colorPrim':heatmap[15],
                'colorSec':heatmap[16],
                'colorTer':heatmap[17],
                'colorBtn':heatmap[18],
                'colorTxtBtn':heatmap[19],
                'orden':json.loads(heatmap[20])
            }

    
            return jsonify({
                'dataDisenio':dataDisenio,
                'dataConf':dataConf
                }),200
            
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

@consultas.route('/contenido/<string:nombre>',methods=['GET'])
def get_contenido(nombre):
    try:
        cur = mysql.connection.cursor()

        sqlDisenio = 'select disenio.idDisenio,disenio.nombre,disenio.idHeader,disenio.idSlide,disenio.idAbout,disenio.idTestimonio,disenio.idBeneficios,disenio.idFormularios,disenio.idFooter,disenio.idConf,disenio.idCampania,disenio.idAccion from disenio,campania,cliente where disenio.idCampania=campania.idCampania and campania.idCliente= cliente.idCliente and disenio.nombre = %s'

        sqlContenido = 'select contenido.idContent, contenido.contenido from contenido,campania, cliente, disenio where contenido.idDisenio=disenio.idDisenio and campania.idCliente=cliente.idCliente and disenio.nombre=%s'

        sqlConf = 'select configuracion.idConf,configuracion.nombreConf,configuracion.colorPrim,configuracion.colorSec,configuracion.colorTer,configuracion.colorBtn,configuracion.colorTxtBtn,configuracion.orden from configuracion, disenio where disenio.idConf = configuracion.idConf and disenio.nombre=%s'


        cur.execute(sqlDisenio,[nombre])
        disenio = cur.fetchone()

        cur.execute(sqlContenido,[nombre])
        contenido = cur.fetchone()

        cur.execute(sqlConf,[nombre])
        configuracion = cur.fetchone()

        dataDisenio = {
            'idDisenio':disenio[0],
            'nombre':disenio[1],
            'idHeader':disenio[2],
            'idSlide':disenio[3],
            'idAbout':disenio[4],
            'idTestimonio':disenio[5],
            'idBeneficios':disenio[6],
            'idFormularios':disenio[7],
            'idFooter':disenio[8],
            'idConf':disenio[9],
            'idCampania':disenio[10],
            'idAccion':disenio[11]
        }
        
        dataConf={
            'idConf':configuracion[0],
            'nombreConf':configuracion[1],
            'colorPrim':configuracion[2],
            'colorSec':configuracion[3],
            'colorTer':configuracion[4],
            'colorBtn':configuracion[5],
            'colorTxtBtn':configuracion[6],
            'orden':json.loads(configuracion[7])
        }

        
        dataContenido = {
            'idContenido':contenido[0],
            'contenido':json.loads(contenido[1])
        }
        
        
        datos = {
            'disenios':dataDisenio,
            'contenido':dataContenido,
            'configuracion':dataConf
        }

        return datos,200
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

@consultas.route('/checkActiveCliente/<idCliente>',methods=['GET'])
def check_active_cliente(idCliente):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select status from campania where idCliente={0}'.format(idCliente));
        status = cur.fetchall()

        result = all(element[0] == 'inactivo' for element in status)

        resultFinalizado = all(element[0] == 'finalizado' for element in status)

        resultSuspendido = all(element[0] == 'suspendido' for element in status)

        if result==True:
            return json.dumps('inactivo'),200
        elif resultFinalizado==True:
            return json.dumps('finalizado'),200
        elif resultSuspendido==True:
            return json.dumps('suspendido'),200
        else: 
            return json.dumps('activo'),200

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

@consultas.route('/checkActiveCampania/<idCampania>',methods=['GET'])
def check_active_campania(idCampania):
    try:
        cur = mysql.connection.cursor();
        cur.execute('select status from disenio where idCampania={0}'.format(idCampania));
        status = cur.fetchall()

        result = all(element[0] == 'inactivo' for element in status)

        if result==True:
            return json.dumps('inactivo'),200
        else: 
            return json.dumps('activo'),200

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