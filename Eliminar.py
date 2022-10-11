from flask import Blueprint
from configuracion import mysql
from helpers import *
import json
import MySQLdb

eliminar = Blueprint('eliminar',__name__)

@eliminar.route('/eliminaCliente/<id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from cliente where idCliente={0}'.format(id))
        mysql.connection.commit()
        return 204
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

@eliminar.route('/eliminarConf/<id>', methods=['DELETE'])
def delete_conf(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from configuracion where idConf={0}'.format(id))
        mysql.connection.commit()
        return 204
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

@eliminar.route('/eliminarDiseño/<id>', methods=['DELETE'])
def delete_disenio(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from disenio where idDisenio={0}'.format(id))
        mysql.connection.commit()
        return 204
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

@eliminar.route('/eliminarCampaña<id>', methods=['DELETE'])
def delete_campania(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from campania where idCampania={0}'.format(id))
        mysql.connection.commit()
        return 204
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

@eliminar.route('/eliminarUsuario<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        cur = mysql.connection.cursor();
        cur.execute('delete from usuarios where idUsuario={0} and superUsuario=0'.format(id))
        mysql.connection.commit()
        return 204
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
