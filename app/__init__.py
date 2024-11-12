import os
import logging
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración de logs
    app.config['UPLOAD_FOLDER'] = 'app/uploads'
    app.secret_key = os.urandom(24)  # Necesario para las sesiones y mensajes flash

    # Configurar el nivel de log
    logging.basicConfig(level=logging.DEBUG)  # Nivel DEBUG, también puedes usar INFO, WARNING, ERROR, CRITICAL

    # También puedes configurar los logs para que se guarden en un archivo
    log_filename = 'app/logs/app.log'
    if not os.path.exists(os.path.dirname(log_filename)):
        os.makedirs(os.path.dirname(log_filename))

    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)  # El nivel de log para el archivo
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(file_handler)

    # Registro del blueprint
    from .routes import main
    app.register_blueprint(main)

    return app

