from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import config

from flask_migrate import Migrate

from flask_mysqldb import MySQL


db = SQLAlchemy() #crea la instancia de sqlalchemy
migrate = Migrate()  # Instancia de Flask-Migrate

def create_app():
    app = Flask(__name__)  # 1. Se crea una instancia de Flask

    # #configuracion del proyecto
    # app.config.from_mapping(
    #     DEBUG = True,   # 2. Activa el modo depuración
    #     SECRET_KEY = 'dev',  # 3. Clave secreta utilizada para sesiones seguras y formularios
    #     SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db" # se crea base de datos
    # )
    #app.config['SECRET_KEY'] = config.HEX_SEC_KEY

    #app.config.from_pyfile('../config.py')
    app.config.from_object(config)

    # Asociar SQLAlchemy y Flask-Migrate a la aplicación
    db.init_app(app) #asocia la instancia de sqlalchemy a la aplicacion flask
    #print("Conectado a la base de datos:", app.config["SQLALCHEMY_DATABASE_URI"])
    migrate.init_app(app, db) 


    #registrar Blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    #registrar Bluprint
    from . import auth
    app.register_blueprint(auth.bp)


    # @app.route('/')  # 4. Define la ruta raíz del proyecto ('/')
    # def index():
    #     return 'hola mundo'   # 5. Devuelve el mensaje 'hola mundo' como respuesta al acceder a la ruta
    # return app       # 6. Devuelve la instancia de la aplicación Flask
    

    @app.route('/')   # 4. Define la ruta raíz del proyecto ('/')
    
    def index():
        return render_template('index.html')   # 5. Devuelve el mensaje 'hola mundo' como respuesta al acceder a la ruta
    

    with app.app_context(): #Creamos las tablas definidas en los modelos de SQLAlchemy dentro del contexto de la aplicación. Esto asegura que la aplicación tenga acceso al entorno adecuado para manipular la base de datos.
        db.create_all()

    return app       # 6. Devuelve la instancia de la aplicación Flask