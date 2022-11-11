#Importacion de librerias
from gettext import textdomain
from configuracion import app,mysql
from Consultas import consultas
from Registros import registros
from Actualizar import actualizar
from Eliminar import eliminar
from formularios import *
from helpers import *
from flask import render_template
import json
from flask import Response,request

app.register_blueprint(consultas, url_prefix='/consultas')
app.register_blueprint(registros, url_prefix='/registros')
app.register_blueprint(actualizar, url_prefix='/actualizar')
app.register_blueprint(eliminar,url_prefix='/eliminar')

#Nota: todas las configuraciones de cross-origin se deben de modificar permitiendo el acceso unicamente
#al front-end, se encuentran en las actualizaciones y registros de la base de datos.

#@app.before_request
#def basic_authentication():
#    if request.method.lower() == 'options':
#        return Response()


@app.route('/prueba/<string:nombre>')
def prueba(nombre):
    cur = mysql.connection.cursor()

    sqlDisenio = 'select disenio.idDisenio,disenio.nombre,disenio.idHeader,disenio.idSlide,disenio.idAbout,disenio.idTestimonio,disenio.idBeneficios,disenio.idFormularios,disenio.idFooter,disenio.idConf,disenio.idCampania,disenio.idAccion from disenio,campania,cliente where disenio.idCampania=campania.idCampania and campania.idCliente= cliente.idCliente and disenio.nombre = %s'

    sqlContenido = 'select  contenido.contenido from contenido,campania, cliente, disenio where contenido.idDisenio=disenio.idDisenio and campania.idCliente=cliente.idCliente and disenio.nombre=%s'

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

    
    dataContenido = json.loads(contenido[0])
    
    datos = {
        'disenios':dataDisenio,
        'contenido':dataContenido,
        'configuracion':dataConf
    }

    return render_template('prueba.html',datos=datos)

@app.route('/landingPage/<string:nombre>')
def landing_page(nombre):

    cur = mysql.connection.cursor()

    sqlDisenio = 'select disenio.idDisenio,disenio.nombre,disenio.idHeader,disenio.idSlide,disenio.idAbout,disenio.idTestimonio,disenio.idBeneficios,disenio.idFormularios,disenio.idFooter,disenio.idConf,disenio.idCampania,disenio.idAccion from disenio,campania,cliente where disenio.idCampania=campania.idCampania and campania.idCliente= cliente.idCliente and disenio.nombre = %s'

    sqlContenido = 'select  contenido.contenido from contenido,campania, cliente, disenio where contenido.idDisenio=disenio.idDisenio and campania.idCliente=cliente.idCliente and disenio.nombre=%s'

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

    
    dataContenido = json.loads(contenido[0])
    
    datos = {
        'disenios':dataDisenio,
        'contenido':dataContenido,
        'configuracion':dataConf
    }

    if dataDisenio['idFormularios']==1:
        opcionFormulario = form_basico()
    
    if dataDisenio['idFormularios']==2:
        opcionFormulario = form_descargas()
    
    if dataDisenio['idFormularios']==3:
        opcionFormulario = form_cita()
    
    if dataDisenio['idFormularios']==4:
        opcionFormulario = form_reservacion()
    
    

    return render_template('landingPage.html',datos=datos, opcionFormulario=opcionFormulario)
    


if __name__=='__main__':
    app.run(debug=True)