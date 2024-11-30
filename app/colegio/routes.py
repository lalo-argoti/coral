from flask import render_template,session
from . import colegio
from .views import *

@colegio.route('/colegio')
def r_portal():
    
    # Aquí podrías obtener datos de la base de datos
    resultados = portal()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('colegio/portal.html', resultados=resultados,  username=session.get('username'))

'''
colegio.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('colegio/matriculas.html', resultados=resultados)
'''
