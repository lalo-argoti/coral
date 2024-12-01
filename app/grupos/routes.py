from flask import render_template,session
from . import grupos
from .views import *

@grupos.route('/grupos')
def r_portal():
   # Aquí podrías obtener datos de la base de datos
    itemsMenu =[{'texto1':'Materias,','texto2':'logros y configuraciones','imagen':'materias.png','link':'materias.r_portal'},
    {'texto1':'Grupos','texto2':'y clubes','imagen':'grupos.png','link':'grupos.distribucion'},
    {'texto1':'Sedes','texto2':'-','imagen':'sedes.png','link':'grupos.sedes'}]
    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Grupos y materias", username=session.get('username'))



@grupos.route('/distribucion')
def distribucion():
    return render_template('grupos/distribucion.html') 



@grupos.route('/sedes')
def sedes():
    # Aquí podrías obtener datos de la base de datos
    # Renderiza una plantilla para mostrar los resultados
    return render_template('grupos/sedes.html')
