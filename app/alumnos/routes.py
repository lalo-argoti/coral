from flask import render_template
from . import alumnos

@alumnos.route('/alumnos')
def lista_alumnos():
    # Aquí podrías obtener datos de la base de datos
    return render_template('alumnos/lista_alumnos.html')
