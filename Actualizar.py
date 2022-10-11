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

@actualizar.route('/modificarUsuario/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_usuario(id):
    nombre = request.json.get('nombre')
    contrasenia = request.json.get('contrasenia')
    
    try:
        sql = 'update usuarios set nombre=%s,contrasenia=%s where idUsuario=%s'
        cur = mysql.connection.cursor();
        cur.execute(sql,(nombre, contrasenia,id))
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

@actualizar.route('/modificaCampaña/<id>', methods=['PUT'])
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

@actualizar.route('/modificaContenidoHeader/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenidoHeader(id):
    whatsapp = request.json.get('whatsapp')
    try:
        cur = mysql.connection.cursor()

        cur.execute('select idHeader from disenio where idDisenio=%s',[id])
        idHeader = eliminarVacios(Convert(str(cur.fetchone())))
        idHeader = eliminarCaracteres(str(idHeader))

        contenido = {'whatsapp':whatsapp}

        sql = 'update contenido set contenido = %s where idDisenio=%s and idSeccion=%s'
        cur.execute(sql,(json.dumps(contenido),id,idHeader))
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

@actualizar.route('/modificaContenidoSlide/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenidoSlide(id):

    try:
        cur = mysql.connection.cursor()

        cur.execute('select idSlide from disenio where idDisenio=%s',[id])
        idSlide = eliminarVacios(Convert(str(cur.fetchone())))
        idSlide = eliminarCaracteres(str(idSlide))

        if idSlide == '1':
            imagenFondo = request.json.get('imagenFondo')
            cta = request.json.get('cta')
            refuerzo = request.json.get('refuerzo')
            colorBoton = request.json.get('colorBoton')
            textoBoton = request.json.get('textoBoton')

            contenido = {
                'imagenFondo':imagenFondo,
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

        sql = 'update contenido set contenido = %s where idDisenio=%s and idSeccion=%s'
        cur.execute(sql,(contenido,id,idSlide))
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

@actualizar.route('/modificaContenidoFormulario/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenido_formulario(id):
    cta = request.json.get('cta')
    refuerzo = request.json.get('refuerzo')
    fondoBoton = request.json.get('fondoBoton')
    textoBoton = request.json.get('textoBoton')
    try:
        cur = mysql.connection.cursor()

        cur.execute('select idFormulario from disenio where idDisenio=%s',[id])
        idFormulario = eliminarVacios(Convert(str(cur.fetchall())))
        idFormulario = eliminarCaracteres(str(idFormulario))

        contenido = {
            'cta':cta,
            'refuerzo':refuerzo,
            'fondoBoton':fondoBoton,
            'textoBoton':textoBoton
            }

        sql = 'update contenido set contenido = %s where idDisenio=%s and idSeccion=%s'
        cur.execute(sql,(contenido,id,idFormulario))
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

@actualizar.route('/modificaContenidoTestimonios/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenido_testimonios(id):
    
    try:
        cur = mysql.connection.cursor()
        cur.execute('select idTestimonio from disenio where idDisenio = {0}'.format(id))
        idTestimonio = eliminarVacios(Convert(str(cur.fetchall())))
        idTestimonio = eliminarCaracteres(str(idTestimonio))

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

        sql = 'update contenido set contenido = %s where idDisenio=%s and idSeccion=%s'
        cur.execute(sql,(contenido,id,idTestimonio))
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

@actualizar.route('/modificaContenidoAbout/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenido_about(id):
    
    try:
        cur = mysql.connection.cursor()

        cur.execute('select idAbout from disenio where idDisenio=%s',[id])
        idAbout = eliminarVacios(Convert(str(cur.fetchall())))
        idAbout = eliminarCaracteres(str(idAbout))

        if idAbout == '1' or idAbout == '2' or idAbout == '3' or idAbout=='4':
            titulo = request.json.get('titulo')
            parrafo = request.json.get('parrafo')
            textoEnriquecido1 = request.json.get('textoEnriquecido1')
            textoEnriquecido2 = request.json.get('textoEnriquecido2')
            textoEnriquecido3 = request.json.get('textoEnriquecido3')
            imagen = request.json.get('imagen')

            contenido = {
                'titulo':titulo,
                'parrafo':parrafo,
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
            imagen = request.json.get('imagen')
            imagen2 = request.json.get('imagen2')
            imagen3 = request.json.get('imagen3')

            contenido = {
                'titulo':titulo,
                'parrafo':parrafo,
                'textoEnriquecido1':textoEnriquecido1,
                'textoEnriquecido2':textoEnriquecido2,
                'textoEnriquecido3':textoEnriquecido3,
                'imagen1':imagen,
                'imagen2':imagen2,
                'imagen3':imagen3
            }


        sql = 'update contenido set contenido = %s where idDisenio=%s and idSeccion=%s'
        cur.execute(sql,(contenido,id,idAbout))
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

@actualizar.route('/modificaContenidoBeneficios/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenido_beneficios(id):
    
    try:
        cur = mysql.connection.cursor()

        cur.execute('select idBeneficios from disenio where idDisenio=%s',[id])
        idBeneficios = eliminarVacios(Convert(str(cur.fetchall())))
        idBeneficios = eliminarCaracteres(str(idBeneficios))

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

        sql = 'update contenido set contenido = %s where idDisenio=%s and idSeccion=%s'
        cur.execute(sql,(contenido,id,idBeneficios))
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


@actualizar.route('/modificaContenidoFooter/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenido_footer(id):
    dominio = request.json.get('dominio')

    try:
        cur = mysql.connection.cursor()

        cur.execute('select idFooter from disenio where idDisenio=%s',[id])
        idFooter = eliminarVacios(Convert(str(cur.fetchall())))
        idFooter = eliminarCaracteres(str(idFooter))

        contenido = {
            'dominio':dominio
        }

        sql = 'update contenido set contenido = %s where idDisenio=%s and idSeccion=%s'
        cur.execute(sql,(contenido,id,idFooter))
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

@actualizar.route('/modificaContenidoAccion/<id>', methods=['PUT'])
@cross_origin(origin='*',headers=['Authorization'])
def update_contenido_accion(id):

    try:
        cur = mysql.connection.cursor()

        cur.execute('select idAccion from disenio where idDisenio=%s',[id])
        idAccion = eliminarVacios(Convert(str(cur.fetchall())))
        idAccion = eliminarCaracteres(str(idAccion))

        if idAccion == '1' or idAccion=='2' or idAccion=='3':
            imagenFondo = request.json.get('imagenFondo')
            cta = request.json.get('cta')
            refuerzo = request.json.get('refuerzo')
            colorBoton = request.json.get('colorBoton')
            textoBoton = request.json.get('textoBoton')
            
            contenido = {
                'imagenFondo':imagenFondo,
                'cta':cta,
                'refuerzo':refuerzo,
                'colorBoton':colorBoton,
                'textoBoton':textoBoton
            }

        if idAccion == '4':
            refuerzo = request.json.get('refuerzo')
            colorBoton = request.json.get('colorBoton')
            textoBoton = request.json.get('textBoton')

            contenido = {
                'refuerzo':refuerzo,
                'colorBoton':colorBoton,
                'textoBoton':textoBoton
            }

        sql = 'update contenido set contenido = %s where idDisenio=%s and idSeccion=%s'
        cur.execute(sql,(contenido,id,idAccion))
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