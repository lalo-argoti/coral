import os
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from werkzeug.utils import secure_filename

# Crear un blueprint para la aplicación
main = Blueprint('main', __name__)

# Datos ficticios para las entradas del blog
blog_entries = [
    {'title': 'Entrada 1', 'content': 'Contenido de la primera entrada del blog.'},
    {'title': 'Entrada 2', 'content': 'Contenido de la segunda entrada del blog.'},
    {'title': 'Entrada 3', 'content': 'Contenido de la tercera entrada del blog.'},
]

# Configuración para la carga de archivos
UPLOAD_FOLDER = 'app/uploads'  # Carpeta donde se guardarán los archivos subidos
ALLOWED_EXTENSIONS = {'svg'}  # Solo permitimos archivos SVG

# Verifica si el archivo tiene una extensión permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ruta principal (index) de la app
@main.route('/', methods=['GET', 'POST'])
def index():
    mensaje = ''
    if request.method == 'POST':
        # Aquí puedes validar el login (por simplicidad no se hace)
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "admin":
            mensaje = "Bienvenido!"
        else:
            mensaje = "Credenciales incorrectas."
    return render_template('index.html', mensaje=mensaje, blog_entries=blog_entries)

# Ruta para login
@main.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "admin":
            return redirect(url_for('main.index'))  # Redirigir al home si el login es correcto
        else:
            mensaje = "Credenciales incorrectas."
    return render_template('login.html', mensaje=mensaje)

# Ruta para cargar imágenes
@main.route('/imagenes', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files.get('file')
        
        if file:
            current_app.logger.debug(f"Archivo recibido: {file.filename}")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            current_app.logger.debug(f"Guardando archivo en: {file_path}")
            try:
                file.save(file_path)
                flash(f'Archivo {filename} subido correctamente!', 'success')
                current_app.logger.info(f'Archivo {filename} subido correctamente')
            except Exception as e:
                flash(f'Error al guardar el archivo: {e}', 'error')
                current_app.logger.error(f'Error al guardar el archivo {filename}: {e}')
        else:
            flash('Solo se permiten archivos SVG.', 'error')
            current_app.logger.warning('Intento de subir un archivo no SVG.')

    return render_template('upload_image.html')

