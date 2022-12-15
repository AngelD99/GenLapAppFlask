from flask_mysqldb import MySQL
from flask_mail import Mail
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from os.path import join, dirname, realpath
import socket

app = Flask(__name__,static_url_path='/static')
#Coneccion con la base de datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='tacticPage'

#Configuracion de Mailtrap
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '365e337513d2da'
app.config['MAIL_PASSWORD'] = '0b2c9757e4b970'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

app.config['SERVER_NAME'] = "localhost:5000"

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/images/..')
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024 
app.config['CORS_HEADERS'] = 'Content-Type'

bootstrap = Bootstrap5(app)
mail=Mail(app)
mysql = MySQL(app)
app.config["JWT_SECRET_KEY"] = "super-secret" 
jwt = JWTManager(app)

#Configurar el origen a la direccion del front
CORS(app,resources={r"/*": {"origins": "*"}})

app.secret_key='mysecretkey';