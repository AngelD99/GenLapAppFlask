#Importacion de librerias
from configuracion import app,mysql
from Consultas import consultas
from Registros import registros
from Actualizar import actualizar
from Eliminar import eliminar
from formularios import *
from helpers import *
from flask import render_template,redirect,url_for
import json
import MySQLdb

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
    print(nombre)
    cur = mysql.connection.cursor()

    sqlCheckStatus = 'SELECT campania.status, disenio.status from campania, disenio where disenio.idCampania=campania.idCampania and disenio.nombre=%s'

    cur.execute(sqlCheckStatus,[nombre])
    status = cur.fetchone()
    
    print(status)

    sqlDisenio = 'select disenio.idDisenio,disenio.nombre,disenio.idHeader,disenio.idSlide,disenio.idAbout,disenio.idTestimonio,disenio.idBeneficios,disenio.idFormularios,disenio.idFooter,disenio.idConf,disenio.idCampania,disenio.idAccion from disenio,campania,cliente where disenio.idCampania=campania.idCampania and campania.idCliente= cliente.idCliente and disenio.nombre = %s'

    sqlContenido = 'select  contenido.contenido from contenido,campania, cliente, disenio where contenido.idDisenio=disenio.idDisenio and campania.idCliente=cliente.idCliente and disenio.nombre=%s'

    sqlConf = 'select configuracion.idConf,configuracion.nombreConf,configuracion.colorPrim,configuracion.colorSec,configuracion.colorTer,configuracion.colorBtn,configuracion.colorTxtBtn,configuracion.orden,(select tipografia from tipografias where configuracion.idTipografia=tipografias.idTipografia) as TipografiaTitulos,(select tipografia from tipografias where configuracion.idTipografiaContent=tipografias.idTipografia) as TipografiaContent from configuracion, disenio where disenio.idConf = configuracion.idConf and disenio.nombre=%s'


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
        'orden':json.loads(configuracion[7]),
        'tipografiaTitulos':configuracion[8],
        'tipografiaContent':configuracion[9]
    }

    
    dataContenido = json.loads(contenido[0])
    
    datos = {
        'disenios':dataDisenio,
        'contenido':dataContenido,
        'configuracion':dataConf
    }

    return datos

@app.route('/landingPage/<string:nombre>', subdomain='<subdominio>')
def landing_page(nombre,subdominio='default'):
    try:
        cur = mysql.connection.cursor()

        sqlCheckStatus = 'SELECT campania.status, disenio.status from campania, disenio where disenio.idCampania=campania.idCampania and disenio.nombre=%s'

        print(subdominio)
        cur.execute(sqlCheckStatus,[nombre])
        status = cur.fetchone()

        if status[0]=='activo':
            if status[1]=='activo':
                sqlDisenio = 'select disenio.idDisenio,disenio.nombre,disenio.idHeader,disenio.idSlide,disenio.idAbout,disenio.idTestimonio,disenio.idBeneficios,disenio.idFormularios,disenio.idFooter,disenio.idConf,disenio.idCampania,disenio.idAccion from disenio,campania,cliente where disenio.idCampania=campania.idCampania and campania.idCliente= cliente.idCliente and disenio.nombre = %s'

                sqlContenido = 'select  contenido.contenido from contenido,campania, cliente, disenio where contenido.idDisenio=disenio.idDisenio and campania.idCliente=cliente.idCliente and disenio.nombre=%s'

                sqlConf = 'select configuracion.idConf,configuracion.nombreConf,configuracion.colorPrim,configuracion.colorSec,configuracion.colorTer,configuracion.colorBtn,configuracion.colorTxtBtn,configuracion.orden,(select tipografia from tipografias where configuracion.idTipografia=tipografias.idTipografia) as TipografiaTitulos,(select tipografia from tipografias where configuracion.idTipografiaContent=tipografias.idTipografia) as TipografiaContent from configuracion, disenio where disenio.idConf = configuracion.idConf and disenio.nombre=%s'

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
                    'orden':json.loads(configuracion[7]),
                    'tipografiaTitulos':configuracion[8],
                    'tipografiaContent':configuracion[9]
                }

                
                dataContenido = json.loads(contenido[0])
                
                datos = {
                    'disenios':dataDisenio,
                    'contenido':dataContenido,
                    'configuracion':dataConf
                }

                if dataDisenio['idFormularios']==1 or dataDisenio['idSlide']==4:
                    opcionFormulario = form_basico()
                
                if dataDisenio['idFormularios']==2:
                    opcionFormulario = form_descargas()
                
                if dataDisenio['idFormularios']==3:
                    opcionFormulario = form_cita()
                
                if dataDisenio['idFormularios']==4 and  dataDisenio['idSlide']!=4:
                    opcionFormulario = form_reservacion()

                return render_template('landingPage.html',datos=datos, opcionFormulario=opcionFormulario)
            else:
                return redirect(url_for('status_inactivo'))
        else:
            return redirect(url_for('status_inactivo'))

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

@app.route('/statusInactivo')
def status_inactivo():
    return render_template('statusInactivo.html')
    
@app.route('/registroExitoso')
def registro_exitoso():
    return render_template('registroExitoso.html')

if __name__=='__main__':
    app.run(debug=True)