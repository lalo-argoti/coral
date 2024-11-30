from flask import render_template
from . import grupos
from .views import *

@grupos.route('/grupos')
def r_portal():
    # Aquí podrías obtener datos de la base de datos
    resultados = portal()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('grupos/portal.html', resultados=resultados)

"""
@alumnos.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/matriculas.html', resultados=resultados)

"""
