
from turtle import color
from flask import Blueprint, request,redirect,url_for
from configuracion import mysql,mail
from helpers import *
import json
import MySQLdb
from flask_cors import cross_origin
from flask_mail import Message
from formularios import *
import os
from werkzeug.utils import secure_filename 

registros = Blueprint('registros',__name__)

@registros.route('/uploadLogo', methods=['POST'])
def fileUpload():
    
    f = request.files['logo']
    filename = secure_filename(f.filename)
    f.save(os.path.join(registros.root_path, 'static/images', 'clientLogos', filename))

    return json.dumps(filename),200

@registros.route('/uploadImgContent/<idDisenio>', methods=['POST'])
def img_content(idDisenio):
    nombreDisenio = ''
    try:
        cur = mysql.connection.cursor()
        cur.execute('select nombre from disenio where idDisenio={0}'.format(idDisenio))
        nombreDisenio = cur.fetchone()[0];
        f = request.files['img']
        filename = secure_filename(f.filename)
        print(f);
        print(nombreDisenio)
        if os.path.isdir(os.path.join(registros.root_path+"\static\images\imagesContent\\"+nombreDisenio)):            
            f.save(os.path.join(registros.root_path, 'static\images', 'imagesContent\\'+nombreDisenio, filename))
        else:
            os.makedirs(os.path.join(registros.root_path+"\static\images\imagesContent\\"+nombreDisenio))
            f.save(os.path.join(registros.root_path, 'static\images', 'imagesContent\\'+nombreDisenio, filename))

        return json.dumps(filename),200
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
    
    

@registros.route('/almacenaUsuario',methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_usuario():
    correo = request.json.get('correo')
    usuario = request.json.get('nombre')
    contrasenia = request.json.get('contrasenia')

    try:
        sql = 'insert into usuarios (correo, usuario, contrasenia, superUsuario) values (%s,%s,%s,0)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(correo,usuario,contrasenia))
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


@registros.route('/almacenaCliente',methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_cliente():
    nombre = request.json.get('nombre')
    logo = request.json.get('logo')
    direccion = request.json.get('direccion')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')
    giro = request.json.get('giro')
    producto = request.json.get('producto')
    user = request.json.get('user')

    try:
        sql = 'insert into cliente (nombre, logo, direccion, telefono, correo, giro, producto,user) values (%s,%s,%s,%s,%s,%s,%s,%s)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(nombre,logo,direccion,telefono,correo,giro,producto,user))
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
    
@registros.route('/almacenaCampania',methods=['POST'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_campania():
    nombre = request.json.get('nombre')
    fechaIni = request.json.get('fechaIni')
    fechaFin = request.json.get('fechaFin')
    idCliente = request.json.get('idCliente')
    status = request.json.get('status')
    user = request.json.get('user')

    try:
        sql = 'insert into campania (nombre, fechaIni,fechaFin,idCliente,status,user) values (%s,%s,%s,%s,%s,%s)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(nombre,fechaIni,fechaFin,idCliente,status,user))
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
  
@registros.route('/almacenaConf', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_conf():
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
        sql = 'insert into configuracion (colorPrim, colorSec,colorTer,colorBtn,colorTxtBtn,idTipografia,idTipografiaContent,nombreConf,orden) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(colorPrim,colorSec,colorTer,colorBtn,colorTxtBtn,tipografiaTitulos,tipografiaContent,nombre,orden))
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
        

@registros.route('/registrarInfoLP/<int:idDisenio>', methods=['POST'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_info(idDisenio):
    try:
        cur = mysql.connection.cursor()
        cur.execute('select idFormularios from disenio where idDisenio={0}'.format(idDisenio))
        idForm = eliminarCaracteres(str(cur.fetchone()))

        #el correo sender probablemente sera un correo de muchaweb.
        #el recipiente se debe de obtener de la base de datos, debe ser del cliente a quien le pertenece el correo
        if idForm == '1':
            form = form_basico();
            if(form.validate_on_submit):
                nombre = form.nombre.data
                correo = form.correo.data
                telefono = form.telefono.data

                datos = {
                    'nombre':nombre,
                    'correo':correo,
                    'telefono':telefono
                    }
                print('entro')
                #msg = Message('Prueba flask gmail', sender = 'elqueenviaCorreo@gmail.com', recipients = ['correoAEnviar@gmail.com'])
                #msg.body = "Cuerpo del correo a enviar"
                #mail.send(msg)

        if idForm == '2':
            form = form_descargas();
            if form.validate_on_submit:
                nombre = form.nombre.data
                correo = form.correo.data

                datos = {
                    'nombre':nombre,
                    'correo':correo
                    }
                #msg = Message('Prueba flask gmail', sender = 'elqueenviaCorreo@gmail.com', recipients = ['correoAEnviar@gmail.com'])
                #msg.body = "Cuerpo de correo a enviar"
                #mail.send(msg)


        if idForm == '3':
            form = form_cita()

            if form.validate_on_submit:
                nombre = request.json.get('nombre')
                correo = request.json.get('correo')
                telefono = request.json.get('telefono')
                horario = request.json.get('horario')
                fecha = request.json.get('fecha')

                datos = {
                    'nombre':nombre,
                    'correo':correo,
                    'telefono':telefono,
                    'horario':horario,
                    'fecha':fecha
                    }

                #msg = Message('Prueba flask gmail', sender = 'elqueenviaCorreo@gmail.com', recipients = ['correoAEnviar@gmail.com'])
                #msg.body = "Cuerpo del correo a enviar"
                #mail.send(msg)

        if idForm == '4':

            form = form_reservacion()

            if form.validate_on_submit():
                nombre = request.json.get('nombre')
                correo = request.json.get('correo')
                destino = request.json.get('destino')
                fechaLlegada = request.json.get('fechaLlegada')
                fechaSalida = request.json.get('fechaSalida')
                numDias = request.json.get('numDias')
                numNinios = request.json.get('numNinios')
                numAdultos = request.json.get('numAdultos')

                datos = {
                    'nombre':nombre,
                    'correo':correo,
                    'destino':destino,
                    'fechaLlegada':fechaLlegada,
                    'fechaSalida':fechaSalida,
                    'numDias':numDias,
                    'numNinios':numNinios,
                    'numAdultos':numAdultos
                    }

                #msg = Message('Prueba flask gmail', sender = 'elqueenviaCorreo@gmail.com', recipients = ['correoAEnviar@gmail.com'])
                #msg.body = "Cuerpo del correo a enviar"
                #mail.send(msg)

        sql='insert into infoFormulario (idDisenio,idFormulario,datosIngresados) values (%s,%s,%s)'
        cur.execute(sql,(idDisenio,int(idForm),json.dumps(datos)))
        mysql.connection.commit()
        return redirect(url_for('registro_exitoso')) ,200

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

@registros.route('/almacenaDisenio', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_disenio():
    nombre = request.json.get('nombre')
    idCampania = request.json.get('idCampania')
    idHeader = request.json.get('header')
    idSlide = request.json.get('slide')
    idAbout = request.json.get('about')
    idFormulario = request.json.get('formulario')
    idTestimonio = request.json.get('testimonios')
    idBeneficio = request.json.get('beneficios')
    idAccion = request.json.get('accion')
    idFooter = request.json.get('footer')
    idConf = request.json.get('configuracion')
    status = request.json.get('status')

    try:
        sql = 'insert into disenio (nombre, idCampania,idHeader,idSlide,idAbout,idFormularios,idTestimonio,idBeneficios,idFooter,idConf,idAccion,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(nombre,idCampania,idHeader,idSlide,idAbout,idFormulario,idTestimonio,idBeneficio,idFooter,idConf,idAccion,status))
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
    

@registros.route('/registrarContenido/<idDisenio>', methods=['GET','POST'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_header(idDisenio):
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

        sql = 'insert into contenido (idDisenio, contenido) values (%s,%s)'
        cur.execute(sql,(idDisenio,json.dumps(contenido)))
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
    