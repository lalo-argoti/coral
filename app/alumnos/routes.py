from flask import render_template
from . import alumnos
from .views import obtener_lista_alumnos

@alumnos.route('/alumnos')
def lista_alumnos():
    # Aquí podrías obtener datos de la base de datos
    resultados = obtener_lista_alumnos()

    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/lista_alumnos.html', resultados=resultados)
