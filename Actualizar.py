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
        cur = mysql.connection.cursor();
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
    nombreConf = request.json.get('nombreConf')
    colorPrim = request.json.get('colorPrim')
    colorSec = request.json.get('colorSec')
    tipografia =request.json.get('tipografia')
    
    try:
        sql = 'update configuracion set nombreConf=%s,colorPrim=%s,colorSec=%s,idTipografia=%s where idConf=%s'
        cur = mysql.connection.cursor();
        cur.execute(sql,(nombreConf,colorPrim,colorSec,tipografia,id))
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

@actualizar.route('/modificaDiseño/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_disenio(id):
    nombre = request.json.get('nombre')
    idHeader = request.json.get('header')
    idSlide = request.json.get('slide')
    idAbout = request.json.get('about')
    idFormulario = request.json.get('formulario')
    idTestimonio = request.json.get('testimonio')
    idBeneficio = request.json.get('beneficio')
    idFooter = request.json.get('footer')
    idConf = request.json.get('configuracion')
    
    try:
        sql = 'update disenio set nombre=%s,idHeader=%s,idSlide=%s,idAbout=%s,idTestimonio=%s,idBeneficios=%s,idFormularios=%s,idFooter=%s,idConf=%s where idDisenio=%s'
        cur = mysql.connection.cursor();
        cur.execute(sql,(nombre,idHeader,idSlide,idAbout,idFormulario,idTestimonio,idBeneficio,idFormulario,idFooter,idConf,id))
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
        contenidoStyle = request.json.get('contentStyle');

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