from flask import render_template,session
from . import materias
from .views import *

@materias.route('/materias')
def r_portal():
    # Aquí podrías obtener datos de la base de datos
    menu = [
    {'texto1': 'Distribución', 'texto2': 'de horarios', 'imagen': 'distribucion.png', 'link': 'grupos.distribucion'},
    {'texto1': 'Logros', 'texto2': 'académicos', 'imagen': 'logros.png', 'link': 'materias.logros'},
    {'texto1': 'Evaluaciones', 'texto2': 'y calificaciones', 'imagen': 'evaluaciones.png', 'link': 'materias.evaluaciones'}
    ]

    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=menu,  username=session.get('username'))
@materias.route('/logros')
def logros():
   return ""

@materias.route('/evaluaciones')
def evaluaciones():
   return ""

'''
colegio.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('colegio/matriculas.html', resultados=resultados)
'''
