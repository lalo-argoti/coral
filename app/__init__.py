import os
import logging
from flask import Flask

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

    # Registro de los blueprints
    from app.core import core
    from app.alumnos import alumnos

    app.register_blueprint(core)
    app.register_blueprint(alumnos)

    return app
