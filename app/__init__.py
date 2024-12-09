import os
import logging
from flask import Flask, jsonify

def create_app():
    # Definir las rutas de las carpetas 'static' y 'templates' para core
    static_folder = os.path.join(os.getcwd(), 'app/core/static')
    template_folder = os.path.join(os.getcwd(), 'app/core/templates')

    # Crear la aplicación Flask especificando las carpetas personalizadas
    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    # Configuración de logs
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'app/uploads')
    app.secret_key = os.urandom(24)

    # Configurar el nivel de log
    logging.basicConfig(level=logging.DEBUG)

    # Configurar logs para archivo
    log_filename = os.path.join(os.getcwd(), 'app/logs/app.log')
    if not os.path.exists(os.path.dirname(log_filename)):
        os.makedirs(os.path.dirname(log_filename))

    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(file_handler)

    #importar y  registro de los blueprints
    from app.core import core
    from app.alumnos import alumnos
    from app.matriculas import matriculas
    from app.colegio import colegio
    from app.grupos import grupos
    from app.usuario import usuario
    from app.materias import materias
    from app.coral import coral
    from app.sesion import sesion 
    from app.user_group import  user_group
    from app.buscar import buscar
    app.register_blueprint(core)
    app.register_blueprint(sesion)
    app.register_blueprint(usuario)
    app.register_blueprint(grupos)
    app.register_blueprint(alumnos)
    app.register_blueprint(matriculas)
    app.register_blueprint(colegio)
    app.register_blueprint(materias)
    app.register_blueprint(coral)
    app.register_blueprint(user_group)
    app.register_blueprint(buscar)
    return app
