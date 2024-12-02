from flask import render_template,session
from . import colegio
from .views import *

@colegio.route('/colegio')
def r_portal():
    # Aquí podrías obtener datos de la base de datos
    menu = [
    {'texto1': 'Docentes', 'texto2': 'y personal', 'imagen': 'docentes.png', 'link': 'colegio.docentes'},
    {'texto1': 'Decretos', 'texto2': 'legales', 'imagen': 'decretos.png', 'link': 'colegio.decretos'},
    {'texto1': 'Eventos', 'texto2': 'y actividades', 'imagen': 'eventos.png', 'link': 'colegio.eventos'}]

    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=menu, username=session.get('username'))

'''
colegio.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('colegio/matriculas.html', resultados=resultados)
'''
