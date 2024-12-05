from flask import render_template,session, redirect, url_for
from . import usuario
from .views import *

@usuario.route('/config')
def r_config():
    return render_template('usuario/portal.html', titulo='Configuración', resultados=['Edita tus ajustes aquí.'], username=session.get('username'))

@usuario.route('/usuario')
def r_portal():
    itemsMenu =[{'texto1':'SQL','texto2':'','imagen':'2.png','link':'coral.databases'},
    {'texto1':'Tablas','texto2':'y datos SQL','imagen':'1.png','link':'coral.tablas'}]
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Matrículas", username=session.get('username'))

@usuario.route('/salir')
def r_salir():
    session.pop('username', None)
    return redirect(url_for('core.r_portal', mensaje="Sesion cerrada"))
