#Importacion de librerias
from gettext import textdomain
from configuracion import app,mysql
from Consultas import consultas
from Registros import registros
from Actualizar import actualizar
from Eliminar import eliminar
from formularios import form_basico, form_descargas
from helpers import *
from flask import render_template
import json

app.register_blueprint(consultas, url_prefix='/consultas')
app.register_blueprint(registros, url_prefix='/registros')
app.register_blueprint(actualizar, url_prefix='/actualizar')
app.register_blueprint(eliminar,url_prefix='/eliminar')

#Nota: todas las configuraciones de cross-origin se deben de modificar permitiendo el acceso unicamente
#al front-end, se encuentran en las actualizaciones y registros de la base de datos.

@app.route('/landingPage/<string:nombre>')
def landing_page(nombre):
    secciones = {}

    cur = mysql.connection.cursor()

    sqlDisenio = 'select * from disenio,cliente where disenio.idCliente=cliente.idCliente and disenio.nombre = %s'

    sqlContenido = 'select contenido.idSeccion, contenido.tipoContenido, contenido.contenido, contenido.seccion  from contenido, cliente, disenio where contenido.idDisenio=disenio.idDisenio and disenio.idCliente=cliente.idCliente and disenio.nombre=%s'

    sqlColores = 'select colorPrim, colorSec from configuracion, cliente where configuracion.idCliente = cliente.idCliente and disenio.nombre=%s'

    sqlHeader = 'select correo, telefono,logo, direccion from cliente,disenio where disenio.idCliente=cliente.idCliente and disenio.nomnbre=%s'

    cur.execute(sqlHeader)
    header = cur.fetchone()

    cur.execute(sqlDisenio,[nombre])
    disenioAux = cur.fetchone()

    cur.execute(sqlContenido,[nombre])
    contenido = cur.fetchall()

    cur.execute(sqlColores,[nombre])
    colores = eliminarVacios(Convert(str(cur.fetchall())))

    colores = eliminarEspacios(str(colores))

    disenio = eliminarVacios(Convert(str(disenioAux)))

    disenio = eliminarEspacios(str(disenio))

    colorPrimario = colores[0]
    colorSecundario = colores[1]
    
    for cont in contenido:
        if cont[3]=='header' and disenio[1]==1 and cont[2] != '':
            contenidoHeader=json.loads(cont[2])
            secciones['header']=False
            
        if cont[3]=='slide' and cont[2] != '':
            contenidoSlide = json.loads(cont[2])
            secciones['slide']=False
        
        if cont[3] =='formulario' and cont[2] != '':
            contenidoFormulario = json.loads(cont[2])
            secciones['formulario']=False
            
        if cont[3] == 'testimonio' and cont[2] != '':
            contenidoTestimonio = json.loads(cont[2])
            secciones['testimonio']=False

        if cont[3] == 'accion' and cont[2] != '':
            contenidoAccion = json.loads(cont[2])
            secciones['accion']=False
        
        if cont[3] == 'about' and cont[2] != '':
            contenidoAbout = json.loads(cont[2])
            secciones['about']=False
           
        if cont[3] == 'beneficios' and cont[2] != '':
            contenidoBeneficios = json.loads(cont[2])
            secciones['beneficios']=False
        
        if cont[3] == 'footer' and cont[2] != '':
            contenidoFooter = json.loads(cont[2])
            secciones['footer']=False
        
        if cont[1] == 'style' and cont[2] != '':
            style = cont[2]


    if disenio[2] == '1':
        opcionFormulario=form_basico()

    if disenio[2] == '2':
        opcionFormulario=form_descargas()

    styleBackground= 'style=background-color:{0};'.format(colorPrimario)
    styleColor='style=color:{0}'.format(colorSecundario)

    secciones = str(secciones)

    return render_template('landingPage.html',
    #fondos de configuracion
    styleBackground=styleBackground,styleColor=styleColor,
    disenio=disenio, secciones=secciones, style=style,
    #contenido de header
    contenidoHeader=contenidoHeader,header=header,
    #contenido slide
    contenidoSlide=contenidoSlide,
    #contenido formulario
    contenidoFormulario=contenidoFormulario,opcionFormulario=opcionFormulario,
    #contenido testimonios
    contenidoTestimonio = contenidoTestimonio,
    #contenido accion
    contenidoAccion = contenidoAccion,
    #contenido about
    contenidoAbout = contenidoAbout,
    #contenido beneficios
    contenidoBeneficios = contenidoBeneficios,
    #contenido footer
    contenidoFooter = contenidoFooter
    )

@app.route('/prueba',methods=['GET'])
def prueba():
    style = 'section{height: 300px;}'
    return render_template('prueba.html',dato='prueba',style=style)

if __name__=='__main__':
    app.run(debug=True)