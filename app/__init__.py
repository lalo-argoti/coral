import os
import logging
from flask import Flask

def create_app():
    # Definir las rutas de las carpetas 'static' y 'templates'
    static_folder = os.path.join(os.getcwd(), 'app/core/static')  # Ruta a la carpeta 'static'
    template_folder = os.path.join(os.getcwd(), 'app/core/templates')  # Ruta a la carpeta 'templates'

    # Crear la aplicación Flask especificando las carpetas personalizadas
    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    # Configuración de logs
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'app/uploads')  # Ruta para subidas
    app.secret_key = os.urandom(24)  # Necesario para las sesiones y mensajes flash

    # Configurar el nivel de log
    logging.basicConfig(level=logging.DEBUG)  # Nivel DEBUG (puedes usar INFO, WARNING, etc.)

    # Configurar logs para archivo
    log_filename = os.path.join(os.getcwd(), 'app/logs/app.log')  # Ruta al archivo de logs
    if not os.path.exists(os.path.dirname(log_filename)):
        os.makedirs(os.path.dirname(log_filename))

    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(file_handler)

    # Registro del blueprint
    from .routes import main  # Importa el blueprint desde routes.py
    app.register_blueprint(main)

    return app
