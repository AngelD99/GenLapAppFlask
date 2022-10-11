
from turtle import color
from flask import Blueprint, request
from configuracion import mysql,mail
from helpers import *
import json
import MySQLdb
from flask_cors import cross_origin
from flask_mail import Message

registros = Blueprint('registros',__name__)

@registros.route('/almacenaUsuario',methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_usuario():
    usuario = request.json.get('nombre')
    contrasenia = request.json.get('contrasenia')

    try:
        sql = 'insert into usuarios (usuario, contrasenia, superUsuario) values (%s,%s,0)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(usuario,contrasenia))
        mysql.connection.commit()
        return 200
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
    try:
        sql = 'insert into cliente (nombre, logo, direccion, telefono, correo, giro, producto) values (%s,%s,%s,%s,%s,%s,%s)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(nombre,logo,direccion,telefono,correo,giro,producto))
        mysql.connection.commit()
        return 200
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
    
@registros.route('/almacenaCampania')
@cross_origin(origin='*',headers=['Authorization'])
def insert_campania():
    nombre = request.json('campania')
    fechaIni = request.json('fechaIni')
    fechaFin = request.json('fechaFin')
    idCliente = request.json('idCliente')
    try:
        sql = 'insert into campania (nombre, fechaIni,fechaFin,idCliente) values (%s,%s,%s,%s)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(nombre,fechaIni,fechaFin,idCliente))
        mysql.connection.commit()
        return 200
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
  
@registros.route('/almacenaConf', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_conf():
    nombre = request.json.get('nombre')
    colorPrim = request.json.get('colorPrim')
    colorSec = request.json.get('colorSec')
    idCliente = request.json.get('idCliente')
    orden = request.json.get('orden')
    
    try:
        sql = 'insert into configuracion (colorPrim, colorSec,idCliente,nombre,orden) values (%s,%s,%s,%s,%s)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(colorPrim,colorSec,idCliente,nombre,orden))
        mysql.connection.commit()
        return 200
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
        

@registros.route('/registrarInfoLP/<string:idDisenio>')
@cross_origin(origin='*',headers=['Authorization'])
def insert_info(idDisenio):
    try:
        cur = mysql.connection.cursor()
        cur.execute('select idFormulario from disenio where idDisenio={0}'.format(idDisenio))
        idForm = eliminarCaracteres(str(cur.fetchone()))

        cur.execute('select elementos from testimonios where idTestimonio={0}'.format(idForm))
        contenidoForm = eliminarVacios(Convert(str(cur.fetchall())))

        sql='insert into infoFormulario (idDisenio,idFormulario,elementosFormulario,datosIngresados) values (%s,%s,%s,%s)'

        #el correo sender probablemente sera un correo de muchaweb.
        #el recipiente se debe de obtener de la base de datos, debe ser del cliente a quien le pertenece el correo
        if idForm == '1':
            nombre = request.json.get('nombre')
            correo = request.json.get('correo')
            telefono = request.json.get('telefono')

            datos = {
                'nombre':nombre,
                'correo':correo,
                'telefono':telefono
                }

            msg = Message('Prueba flask gmail', sender = 'elqueenviaCorreo@gmail.com', recipients = ['correoAEnviar@gmail.com'])
            msg.body = "Cuerpo del correo a enviar"
            mail.send(msg)

        if idForm == '2':
            nombre = request.json.get('nombre')
            correo = request.json.get('correo')

            datos = {
                'nombre':nombre,
                'correo':nombre
                }

            msg = Message('Prueba flask gmail', sender = 'elqueenviaCorreo@gmail.com', recipients = ['correoAEnviar@gmail.com'])
            msg.body = "Cuerpo de correo a enviar"
            mail.send(msg)


        if idForm == '3':
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

            msg = Message('Prueba flask gmail', sender = 'elqueenviaCorreo@gmail.com', recipients = ['correoAEnviar@gmail.com'])
            msg.body = "Cuerpo del correo a enviar"
            mail.send(msg)

        if idForm == '4':
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

            msg = Message('Prueba flask gmail', sender = 'elqueenviaCorreo@gmail.com', recipients = ['correoAEnviar@gmail.com'])
            msg.body = "Cuerpo del correo a enviar"
            mail.send(msg)

        cur.execute(sql,idDisenio,idForm,json.dumps(contenidoForm),json.dumps(datos))
        mysql.connection.commit()
        return 200

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

@registros.route('/almacenaDiseño', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_disenio():
    nombre = request.json.get('nombre')
    idCampania = request.json.get('campania')
    idHeader = request.json.get('header')
    idSlide = request.json.get('slide')
    idAbout = request.json.get('about')
    idFormulario = request.json.get('formulario')
    idTestimonio = request.json.get('testimonio')
    idBeneficio = request.json.get('beneficio')
    idFooter = request.json.get('footer')
    idConf = request.json.get('configuracion')

    try:
        sql = 'insert into disenio (nombre, idCampania,idHeader,idSlide,idAbout,idFormularios,idTestimonios,idBeneficio,idFooter,idConf) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur = mysql.connection.cursor()
        cur.execute(sql,(nombre,idCampania,idHeader,idSlide,idAbout,idFormulario,idTestimonio,idBeneficio,idFooter,idConf))
        mysql.connection.commit()
        return 200
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
    

@registros.route('/registrarContentHeader/<string:idDisenio>', methods=['GET','POST'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_header(idDisenio):
    whatsapp = request.json.get('whatsapp')

    try:
        cur = mysql.connection.cursor()

        cur.execute('select idHeader from disenio where idDisenio=%s',[idDisenio])
        idHeader = eliminarVacios(Convert(str(cur.fetchall())))
        idHeader = eliminarCaracteres(str(idHeader))

        cur.execute('select elementos from header where idHeader=%s',[idHeader])
        tipoContenido = eliminarVacios(Convert(str(cur.fetchall())))

        contenido = {'whatsapp':whatsapp}

        sql = 'insert into contenido (idDisenio,idSeccion,tipoContenido, contenido) values (%s,%s,%s,%s)'
        cur.execute(sql,(idDisenio,idHeader,json.dumps(tipoContenido),json.dumps(contenido)))
        mysql.connection.commit()
        return 200
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
    

@registros.route('/registrarContentTestimonio/<string:idDisenio>', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_testimonio(idDisenio):
    try:
        cur = mysql.connection.cursor()
        cur.execute('select idTestimonio from disenio where idDisenio = {0}'.format(idDisenio))
        idTestimonio = eliminarVacios(Convert(str(cur.fetchall())))
        idTestimonio = eliminarCaracteres(str(idTestimonio))

        cur.execute('select elementos from testimonios where idTestimonio={0}'.format(idTestimonio))
        tipoContenido = eliminarVacios(Convert(str(cur.fetchall())))

        if idTestimonio == '1':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            testimonio1 = request.json.get('testimonio1')
            icono1 = request.json.get('icono1')
            tituloTestimonio1 = request.json.get('tituloTestimonio1')
            locacionTestimonio1 = request.json.get('locacionTestimonio1')

            testimonio2 = request.json.get('testimonio2')
            icono2 = request.json.get('icono2')
            tituloTestimonio2 = request.json.get('tituloTestimonio2')
            locacionTestimonio2 = request.json.get('locacionTestimonio2')

            testimonio3 = request.json.get('testimonio3')
            icono3 = request.json.get('icono3')
            tituloTestimonio3 = request.json.get('tituloTestimonio3')
            locacionTestimonio3 = request.json.get('locacionTestimonio3')

            testimonio4 = request.json.get('testimonio4')
            icono4 = request.json.get('icono4')
            tituloTestimonio4 = request.json.get('tituloTestimonio4')
            locacionTestimonio4 = request.json.get('locacionTestimonio4')

            testimonio5 = request.json.get('testimonio5')
            icono5 = request.json.get('icono5')
            tituloTestimonio5 = request.json.get('tituloTestimonio5')
            locacionTestimonio5 = request.json.get('locacionTestimonio5')

            testimonio6 = request.json.get('testimonio6')
            icono6 = request.json.get('icono6')
            tituloTestimonio6 = request.json.get('tituloTestimonio6')
            locacionTestimonio6 = request.json.get('locacionTestimonio6')
            
            contenido = {
                'titulo': titulo,
                'parrafo':parrafo, 
                'testimonio1':testimonio1,
                'icono1':icono1,
                'tituloTestimonio1':tituloTestimonio1,
                'locacionTestimonio1':locacionTestimonio1,
                'testimonio2':testimonio2,
                'icono2':icono2,
                'tituloTestimonio2':tituloTestimonio2,
                'locacionTestimonio2':locacionTestimonio2,
                'testimonio3':testimonio3,
                'icono3':icono3,
                'tituloTestimonio3':tituloTestimonio3,
                'locacionTestimonio3':locacionTestimonio3,
                'testimonio4':testimonio4,
                'icono4':icono4,
                'tituloTestimonio4':tituloTestimonio4,
                'locacionTestimonio4':locacionTestimonio4,
                'testimonio5':testimonio5,
                'icono5':icono5,
                'tituloTestimonio5':tituloTestimonio5,
                'locacionTestimonio5':locacionTestimonio5,
                'testimonio6':testimonio6,
                'icono6':icono6,
                'tituloTestimonio6':tituloTestimonio6,
                'locacionTestimonio6':locacionTestimonio6
                }
        
        if idTestimonio == '2' or idTestimonio=='4':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            icono1 = request.json.get('icono1')
            tituloTestimonio1 = request.json.get('tituloTestimonio1')
            testimonio1 = request.json.get('testimonio1')

            icono2 = request.json.get('icono2')
            tituloTestimonio2 = request.json.get('tituloTestimonio2')
            testimonio2 = request.json.get('testimonio2')

            icono3 = request.json.get('icono3')
            tituloTestimonio3 = request.json.get('tituloTestimonio3')
            testimonio3 = request.json.get('testimonio3')

            icono4 = request.json.get('icono4')
            tituloTestimonio4 = request.json.get('tituloTestimonio4')
            testimonio4 = request.json.get('testimonio4')

            icono5 = request.json.get('icono5')
            tituloTestimonio5 = request.json.get('tituloTestimonio5')
            testimonio5 = request.json.get('testimonio5')

            icono6 = request.json.get('icono6')
            tituloTestimonio6 = request.json.get('tituloTestimonio6')
            testimonio6 = request.json.get('testimonio6')

            contenido = {
                'titulo': titulo,
                'parrafo':parrafo, 
                'testimonio1':testimonio1,
                'icono1':icono1,
                'tituloTestimonio1':tituloTestimonio1,
                'testimonio2':testimonio2,
                'icono2':icono2,
                'tituloTestimonio2':tituloTestimonio2,
                'testimonio3':testimonio3,
                'icono3':icono3,
                'tituloTestimonio3':icono3,
                'testimonio4':testimonio4,
                'icono4':icono4,
                'tituloTestimonio4':tituloTestimonio4,
                'testimonio5':testimonio5,
                'icono5':icono5,
                'tituloTestimonio5':tituloTestimonio5,
                'testimonio6':testimonio6,
                'icono6':icono6,
                'tituloTestimonio6':tituloTestimonio6,
                }
        
        if idTestimonio =='3':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            testimonio1 = request.json.get('testimonio1')
            icono1 = request.json.get('icono1')
            tituloTestimonio1 = request.json.get('tituloTestimonio1')
            locacionTestimonio1 = request.json.get('locacionTestimonio1')

            testimonio2 = request.json.get('testimonio2')
            icono2 = request.json.get('icono2')
            tituloTestimonio2 = request.json.get('tituloTestimonio2')
            locacionTestimonio2 = request.json.get('locacionTestimonio2')

            testimonio3 = request.json.get('testimonio3')
            icono3 = request.json.get('icono3')
            tituloTestimonio3 = request.json.get('tituloTestimonio3')
            locacionTestimonio3 = request.json.get('locacionTestimonio3')

            testimonio4 = request.json.get('testimonio4')
            icono4 = request.json.get('icono4')
            tituloTestimonio4 = request.json.get('tituloTestimonio4')
            locacionTestimonio4 = request.json.get('locacionTestimonio4')

            testimonio5 = request.json.get('testimonio5')
            icono5 = request.json.get('icono5')
            tituloTestimonio5 = request.json.get('tituloTestimonio5')
            locacionTestimonio5 = request.json.get('locacionTestimonio5')

            testimonio6 = request.json.get('testimonio6')
            icono6 = request.json.get('icono6')
            tituloTestimonio6 = request.json.get('tituloTestimonio6')
            locacionTestimonio6 = request.json.get('locacionTestimonio6')

            imagen = request.json.get('imagen')
            
            contenido = {
                'titulo': titulo,
                'parrafo':parrafo, 
                'testimonio1':testimonio1,
                'icono1':icono1,
                'tituloTestimonio1':tituloTestimonio1,
                'locacionTestimonio1':locacionTestimonio1,
                'testimonio2':testimonio2,
                'icono2':icono2,
                'tituloTestimonio2':tituloTestimonio2,
                'locacionTestimonio2':locacionTestimonio2,
                'testimonio3':testimonio3,
                'icono3':icono3,
                'tituloTestimonio3':icono3,
                'locacionTestimonio3':locacionTestimonio3,
                'testimonio4':testimonio4,
                'icono4':icono4,
                'tituloTestimonio4':tituloTestimonio4,
                'locacionTestimonio4':locacionTestimonio4,
                'testimonio5':testimonio5,
                'icono5':icono5,
                'tituloTestimonio5':tituloTestimonio5,
                'locacionTestimonio5':locacionTestimonio5,
                'testimonio6':testimonio6,
                'icono6':icono6,
                'tituloTestimonio6':tituloTestimonio6,
                'locacionTestimonio6':locacionTestimonio6,
                'imagen':imagen
                }


        sql = 'insert into contenido (idDisenio,idSeccion,tipoContenido, contenido) values (%s,%s,%s)'
        cur.execute(sql,(idDisenio,idTestimonio,json.dumps(tipoContenido),json.dumps(contenido)))
        mysql.connection.commit()
        return 200
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

@registros.route('/registrarContentFormulario/<string:idDisenio>', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_formulario(idDisenio):
    cta = request.json.get('cta')
    refuerzo = request.json.get('refuerzo')
    fondoBoton = request.json.get('fondoBoton')
    textoBoton = request.json.get('textoBoton')

    try:
        cur = mysql.connection.cursor()

        cur.execute('select idFormulario from disenio where idDisenio=%s',[idDisenio])
        idFormulario = eliminarVacios(Convert(str(cur.fetchall())))
        idFormulario = eliminarCaracteres(str(idFormulario))

        cur.execute('select elementos from formularios where idFormulario=%s',[idFormulario])
        tipoContenido = eliminarVacios(Convert(str(cur.fetchall())))

        contenido = {
            'cta':cta,
            'refuerzo':refuerzo,
            'fondoBoton':fondoBoton,
            'textoBoton':textoBoton
            }

        sql = 'insert into contenido (idDisenio,idSeccion,tipoContenido, contenido) values (%s,%s,%s,%s)'
        cur.execute(sql,(idDisenio,idFormulario,json.dumps(tipoContenido),json.dumps(contenido)))
        mysql.connection.commit()
        return 200
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

@registros.route('/registrarContentSlide/<string:idDisenio>', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_slide(idDisenio):
    try:
        cur = mysql.connection.cursor()

        cur.execute('select idSlide from disenio where idDisenio=%s',[idDisenio])
        idSlide = eliminarVacios(Convert(str(cur.fetchall())))
        idSlide = eliminarCaracteres(str(idSlide))

        if idSlide == '1':
            imagenFondo = request.json.get('imagenFondo')
            logo = request.json.get('logo')
            cta = request.json.get('cta')
            refuerzo = request.json.get('refuerzo')
            colorBoton = request.json.get('colorBoton')
            textoBoton = request.json.get('textoBoton')

            imagenFondo = 'style="background-image: url({0})"'.format(imagenFondo)
            colorBoton = 'style=background-color:{0}'.format(colorBoton)

            contenido = {
                'imagenFondo':imagenFondo,
                'logo':logo,
                'cta':cta,
                'refuerzo':refuerzo, 
                'colorBoton':colorBoton,
                'textoBoton':textoBoton
                }

        if idSlide == '2' or idSlide == '3':
            imagenFondo = request.json.get('imagenFondo')
            logotipo = request.json.get('logotipo')
            cta = request.json.get('cta')
            refuerzo = request.json.get('refuerzo')
            colorBoton = request.json.get('colorBoton')
            textoBoton  = request.json.get('fondoBoton')
            heroe = request.json.get('heroe')

            imagenFondo = 'style="background-image: url({0})"'.format(imagenFondo)
            colorBoton = 'style=background-color:{0}'.format(colorBoton)

            contenido = {
                'imagenFondo':imagenFondo,
                'logotipo':logotipo,
                'cta':cta,
                'refuerzo':refuerzo, 
                'colorBoton':colorBoton,
                'textoBoton':textoBoton,
                'heroe':heroe
                }

        if idSlide == '4':
            imagenFondo = request.json.get('imagenFondo')
            logotipo = request.json.get('logotipo')
            cta = request.json.get('cta')
            refuerzo = request.json.get('refuerzo')
            ctaFormulario = request.json.get('ctaFormulario')
            refuerzoFormulario = request.json.get('refuerzoFormulario')
            colorBoton = request.json.get('colorBoton')
            textoBoton = request.json.get('textoColor')

            imagenFondo = 'style="background-image: url({0})"'.format(imagenFondo)
            colorBoton = 'style=background-color:{0}'.format(colorBoton)

            contenido = {
                'imagenFondo':imagenFondo,
                'logotipo':logotipo,
                'cta':cta,
                'refuerzo':refuerzo, 
                'ctaFormulario':ctaFormulario,
                'refuerzoFormulario':refuerzoFormulario,
                'colorBoton':colorBoton,
                'textoBoton':textoBoton
                }


        cur.execute('select elementos from formularios where idFormulario=%s',[idSlide])
        tipoContenido = eliminarVacios(Convert(str(cur.fetchall())))

        sql = 'insert into contenido (idDisenio,idSeccion,tipoContenido, contenido) values (%s,%s,%s,%s)'
        cur.execute(sql,(idDisenio,idSlide,json.dumps(tipoContenido),json.dumps(contenido)))
        mysql.connection.commit()
        return 200
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

@registros.route('/registrarContentAbout/<string:idDisenio>', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_about(idDisenio):
    try:
        cur = mysql.connection.cursor()

        cur.execute('select idAbout from disenio where idDisenio=%s',[idDisenio])
        idAbout = eliminarVacios(Convert(str(cur.fetchall())))
        idAbout = eliminarCaracteres(str(idAbout))

        cur.execute('select elementos from abouts where idAbout=%s',[idAbout])
        tipoContenido = eliminarVacios(Convert(str(cur.fetchall())))

        if idAbout == '1' or idAbout == '2' or idAbout == '3' or idAbout=='4':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            parrafo2 = request.json.get('parrafo2')
            textoEnriquecido1 = request.json.get('textoEnriquecido1')
            textoEnriquecido2 = request.json.get('textoEnriquecido2')
            textoEnriquecido3 = request.json.get('textoEnriquecido3')
            imagen = request.json.get('imagen')

            contenido = {
                'titulo':titulo,
                'parrafo':parrafo,
                'parrafo2':parrafo2,
                'textoEnriquecido1':textoEnriquecido1,
                'textoEnriquecido2':textoEnriquecido2,
                'textoEnriquecido3':textoEnriquecido3,
                'imagen':imagen
            }
        
        if idAbout=='5':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            textoEnriquecido1 = request.json.get('textoEnriquecido1')
            textoEnriquecido2 = request.json.get('textoEnriquecido2')
            textoEnriquecido3 = request.json.get('textoEnriquecido3')
            imagen1 = request.json.get('imagen1')
            imagen2 = request.json.get('imagen2')
            imagen3 = request.json.get('imagen3')
            
            contenido = {
                'titulo':titulo,
                'parrafo':parrafo,
                'textoEnriquecido1':textoEnriquecido1,
                'textoEnriquecido2':textoEnriquecido2,
                'textoEnriquecido3':textoEnriquecido3,
                'imagen1':imagen1,
                'imagen2':imagen2,
                'imagen3':imagen3
            }

        sql = 'insert into contenido (idDisenio,idSeccion,tipoContenido, contenido) values (%s,%s,%s,%s)'
        cur.execute(sql,(idDisenio,idAbout,json.dumps(tipoContenido),json.dumps(contenido)))
        mysql.connection.commit()
        return 200
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

@registros.route('/registrarContentBeneficios/<string:idDisenio>', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_beneficios(idDisenio):
    try:
        cur = mysql.connection.cursor()

        cur.execute('select idBeneficios from disenio where idDisenio=%s',[idDisenio])
        idBeneficios = eliminarVacios(Convert(str(cur.fetchall())))
        idBeneficios = eliminarCaracteres(str(idBeneficios))

        cur.execute('select elementos from abouts where idAbout=%s',[idBeneficios])
        tipoContenido = eliminarVacios(Convert(str(cur.fetchall())))

        if idBeneficios == '1':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            beneficio1 = request.json.get('beneficio1')
            beneficio2 = request.json.get('beneficio2')
            beneficio3 = request.json.get('beneficio3')
            beneficio4 = request.json.get('beneficio4')
            beneficio5 = request.json.get('beneficio5')        
            beneficio6 = request.json.get('beneficio6')
            imagen1 = request.json.get('imagen1')
            imagen2 = request.json.get('imagen2')
            imagen3 = request.json.get('imagen3')

            contenido = {
                'titulo':titulo,
                'parrafo':parrafo,
                'beneficio1':beneficio1,
                'beneficio2':beneficio2,
                'beneficio3':beneficio3,
                'beneficio4':beneficio4,
                'beneficio5':beneficio5,
                'beneficio6':beneficio6,
                'imagen1':imagen1,
                'imagen2':imagen2,  
                'imagen3':imagen3
                }
        
        if idBeneficios == '2' or idBeneficios == '3' or idBeneficios == '4':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            beneficio1 = request.json.get('beneficio1')
            beneficio2 = request.json.get('beneficio2')
            beneficio3 = request.json.get('beneficio3')
            beneficio4 = request.json.get('beneficio4')
            beneficio5 = request.json.get('beneficio5')        
            beneficio6 = request.json.get('beneficio6')
            imagen = request.json.get('imagen')

            contenido = {
                'titulo':titulo,
                'parrafo':parrafo,
                'beneficio1':beneficio1,
                'beneficio2':beneficio2,
                'beneficio3':beneficio3,
                'beneficio4':beneficio4,
                'beneficio5':beneficio5,
                'beneficio6':beneficio6,
                'imagen':imagen
                }

        if idBeneficios == '5':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            imagenBeneficio1 = request.json.get('imagenBeneficio1')
            tituloBeneficio1 = request.json.het('tituloBeneficio1')
            beneficio1 = request.json.get('beneficio1')
            imagenBeneficio2 = request.json.get('imagenBeneficio2')
            tituloBeneficio2 = request.json.het('tituloBeneficio2')
            beneficio2 = request.json.get('beneficio2')
            imagenBeneficio3 = request.json.get('imagenBeneficio3')
            tituloBeneficio3 = request.json.het('tituloBeneficio3')
            beneficio3 = request.json.get('beneficio3')
            imagenBeneficio4 = request.json.get('imagenBeneficio4')
            tituloBeneficio4 = request.json.het('tituloBeneficio4')
            beneficio4 = request.json.get('beneficio4')
            imagenBeneficio5 = request.json.get('imagenBeneficio5')
            tituloBeneficio5 = request.json.het('tituloBeneficio5')
            beneficio5 = request.json.get('beneficio5')        
            imagenBeneficio6 = request.json.get('imagenBeneficio6')
            tituloBeneficio6 = request.json.het('tituloBeneficio6')
            beneficio6 = request.json.get('beneficio6')

            contenido = {
                'titulo':titulo,
                'parrafo':parrafo,
                'imagenBeneficio1': imagenBeneficio1,
                'tituloBeneficio1': tituloBeneficio1,
                'beneficio1':beneficio1,
                'imagenBeneficio2': imagenBeneficio2,
                'tituloBeneficio2': tituloBeneficio2,
                'beneficio2':beneficio2,
                'imagenBeneficio3': imagenBeneficio3,
                'tituloBeneficio3': tituloBeneficio3,
                'beneficio3':beneficio3,
                'imagenBeneficio4': imagenBeneficio4,
                'tituloBeneficio4': tituloBeneficio4,
                'beneficio4':beneficio4,
                'imagenBeneficio5': imagenBeneficio5,
                'tituloBeneficio5': tituloBeneficio5,
                'beneficio5':beneficio5,
                'imagenBeneficio6': imagenBeneficio6,
                'tituloBeneficio6': tituloBeneficio6,
                'beneficio6':beneficio6
                }
        if idBeneficios == '6':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            tituloBeneficio1 = request.json.het('tituloBeneficio1')
            beneficio1 = request.json.get('beneficio1')
            tituloBeneficio2 = request.json.het('tituloBeneficio2')
            beneficio2 = request.json.get('beneficio2')
            tituloBeneficio3 = request.json.het('tituloBeneficio3')
            beneficio3 = request.json.get('beneficio3')
            tituloBeneficio4 = request.json.het('tituloBeneficio4')
            beneficio4 = request.json.get('beneficio4')
            tituloBeneficio5 = request.json.het('tituloBeneficio5')
            beneficio5 = request.json.get('beneficio5')        
            tituloBeneficio6 = request.json.het('tituloBeneficio6')
            beneficio6 = request.json.get('beneficio6')

            contenido = {
                'titulo':titulo,
                'parrafo':parrafo,
                'tituloBeneficio1': tituloBeneficio1,
                'beneficio1':beneficio1,
                'tituloBeneficio2': tituloBeneficio2,
                'beneficio2':beneficio2,
                'tituloBeneficio3': tituloBeneficio3,
                'beneficio3':beneficio3,
                'tituloBeneficio4': tituloBeneficio4,
                'beneficio4':beneficio4,
                'tituloBeneficio5': tituloBeneficio5,
                'beneficio5':beneficio5,
                'tituloBeneficio6': tituloBeneficio6,
                'beneficio6':beneficio6
                }
                
        sql = 'insert into contenido (idDisenio,idSeccion,tipoContenido, contenido) values (%s,%s,%s,%s)'
        cur.execute(sql,(idDisenio,idBeneficios,json.dumps(tipoContenido),json.dumps(contenido)))
        MySQLdb.connection.commit()
        return 200
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

@registros.route('/registrarContentFooter/<string:idDisenio>', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_footer(idDisenio):
    dominio = request.json.get('dominio')

    try:
        cur = mysql.connection.cursor()

        cur.execute('select idFooter from disenio where idDisenio=%s',[idDisenio])
        idFooter = eliminarVacios(Convert(str(cur.fetchall())))
        idFooter = eliminarCaracteres(str(idFooter))

        cur.execute('select elementos from footer where idHeader=%s',[idFooter])
        tipoContenido = eliminarVacios(Convert(str(cur.fetchall())))

        contenido = {
            'dominio':dominio
        }

        sql = 'insert into contenido (idDisenio,idSeccion,tipoContenido, contenido) values (%s,%s,%s,%s)'
        cur.execute(sql,(idDisenio,idFooter,json.dumps(tipoContenido),json.dumps(contenido)))
        mysql.connection.commit()
        return 200
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

@registros.route('/registrarContentAccion/<string:idDisenio>', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Authorization'])
def insert_contenido_accion(idDisenio):
    try:
        cur = mysql.connection.cursor()

        cur.execute('select idAccion from disenio where idDisenio=%s',[idDisenio])
        idAccion = eliminarVacios(Convert(str(cur.fetchall())))
        idAccion = eliminarCaracteres(str(idAccion))

        cur.execute('select elementos from footer where idHeader=%s',[idAccion])
        tipoContenido = eliminarVacios(Convert(str(cur.fetchall())))

        if idAccion == '1' or idAccion=='2' or idAccion=='3':
            imagenFondo = request.json.get('imagenFondo')
            cta = request.json.get('cta')
            refuerzo = request.json.get('refuerzo')
            colorBoton = request.json.get('colorBoton')
            textoBoton = request.json.get('textoBoton')

            imagenFondo = 'style="background-image: url({0})'.format(imagenFondo)
            colorBoton = 'style=background-color:{0}'.format(colorBoton)
            
            contenido = {
                'imagenFondo':imagenFondo,
                'cta':cta,
                'refuerzo':refuerzo,
                'colorBoton':colorBoton,
                'textoBoton':textoBoton
            }

        if idAccion == '4':
            colorFondo = request.json.get('colorFondo')
            refuerzo = request.json.get('refuerzo')
            colorBoton = request.json.get('colorBoton')
            textoBoton = request.json.get('textBoton')

            colorFondo = 'style=background-color:{0}'.format(colorFondo)
            
            contenido = {
                'colorFondo':colorFondo,
                'refuerzo':refuerzo,
                'colorBoton':colorBoton,
                'textoBoton':textoBoton
            }

        sql = 'insert into contenido (idDisenio,idSeccion,tipoContenido, contenido) values (%s,%s,%s,%s)'
        cur.execute(sql,(idDisenio,idAccion,json.dumps(tipoContenido),json.dumps(contenido)))
        mysql.connection.commit()
        return 200
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
