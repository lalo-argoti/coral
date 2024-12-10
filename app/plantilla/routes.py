from flask import render_template,session
from . import grupos
from .views import *
import ast
@grupos.route('/grupos')
def r_portal():
    # Aquí podrías obtener datos de la base de datos
    resultados = portal()
    # Renderiza una buscar para mostrar los resultados
    return render_template('grupos/portal.html', resultados=resultados, username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

"""
@alumnos.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una buscar para mostrar los resultados
    return render_template('alumnos/matriculas.html', resultados=resultados)

"""
