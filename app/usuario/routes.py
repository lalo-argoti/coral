from flask import render_template,session
from . import usuario
from .views import *

@usuario.route('/config')
def r_config():
    return render_template('usuario/portal.html', titulo='Configuración', resultados=['Edita tus ajustes aquí.'], username=session.get('username'))

@usuario.route('/usuario')
def r_portal():
    #resultados = portal()  # Simula obtener datos
    #return render_template('usuario/portal.html', titulo='Portal', resultados=resultados, username=session.get('username'))
    # Aquí podrías obtener datos de la base de datos
    itemsMenu =[{'texto1':'SQL','texto2':'','imagen':'2.png','link':'coral.databases'},
    {'texto1':'Tablas','texto2':'y datos SQL','imagen':'1.png','link':'coral.tablas'}]
    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Matrículas", username=session.get('username'))



@usuario.route('/salir')
def r_salir():
    return render_template('usuario/portal.html', titulo='Salir', mensaje='Has cerrado sesión.', resultados=[], username=session.get('username'))




"""
@alumnos.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/matriculas.html', resultados=resultados)

"""
