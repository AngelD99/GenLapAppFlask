from flask import Blueprint
from configuracion import mysql
from helpers import *
import MySQLdb
from flask_cors import cross_origin

eliminar = Blueprint('eliminar',__name__)

@eliminar.route('/eliminaCliente/<id>', methods=['DELETE','OPTIONS'])
@cross_origin(origin='*',headers=['Authorization'])
def delete_cliente(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from cliente where idCliente={0}'.format(id))
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

@eliminar.route('/eliminarConf/<id>', methods=['DELETE','OPTIONS'])
@cross_origin(origin='*',headers=['Authorization'])
def delete_conf(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from configuracion where idConf={0}'.format(id))
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

@eliminar.route('/eliminarDiseño/<id>', methods=['DELETE','OPTIONS'])
@cross_origin(origin='*',headers=['Authorization'])
def delete_disenio(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from disenio where idDisenio={0}'.format(id))
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

@eliminar.route('/eliminarCampania/<id>', methods=['DELETE'])
@cross_origin(origin='*',headers=['Authorization'])
def delete_campania(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from campania where idCampania={0}'.format(id))
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

@eliminar.route('/eliminarUsuario/<id>', methods=['DELETE','OPTIONS'])
@cross_origin(origin='*',headers=['Authorization'])
def delete_usuario(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from usuarios where idUsuario={0} and superUsuario=0'.format(id))
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
