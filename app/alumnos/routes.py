from flask import render_template, request, redirect, url_for,session
from . import alumnos
from .views import *

p='/alumnos'

#
#=======
@alumnos.route(p)
def r_portal():
   # Aquí podrías obtener datos de la base de datos
    itemsMenu =[{'texto1':'Matriculas','texto2':'e inscripciones','imagen':'3.png','link':'matriculas.r_portal'},
    {'texto1':'Acudientes','texto2':'y contacto','imagen':'6.png','link':'alumnos.almns_acudientes'},
    {'texto1':'Notas','texto2':'logros y recuperaciones','imagen':'2.png','link':'alumnos.almns_calificaciones'},
    {'texto1':'Grados','texto2':'y promociones','imagen':'5.png','link':'alumnos.almns_promocion'}]
    # Renderiza una buscar para mostrar los resultados
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Alumnos", username=session.get('username'))

#>>>>>>> 3501d088753a561b2bf2d97c390cf716b56db569

@alumnos.route(p+'/calificaciones')
def almns_calificaciones():
    DB(query=f'--accion: calificaciones', username="").run_query()
    resultados = calificaciones()
    return render_template('alumnos/calificaciones.html', resultados=resultados, username=session.get('username'), titulo="estudiantes")

@alumnos.route(p+'/acudientes')
def almns_acudientes():
    resultados= DB(query=f'SELECT * FROM occb_acudientes;', username="").run_query()
    return render_template('core/tabla2.html', datos=resultados,encabezados=["identidad","Nombres","Ocupación","Dirección","Celular","Correo"], username=session.get('username'), titulo="acudientes")

@alumnos.route(p+'/promocion')
def almns_promocion():
    resultados = promocion()
    DB(query="-- desde promocion", username="").run_query()
    return render_template('alumnos/promocion.html', resultados=resultados , username=session.get('username'))

@alumnos.route(p)
def r_portal():
   # Aquí podrías obtener datos de la base de datos
    itemsMenu =[{'texto1':'Matriculas','texto2':'e inscripciones','imagen':'3.png','link':'matriculas.r_portal'},
    {'texto1':'Acudientes','texto2':'y contacto','imagen':'6.png','link':'alumnos.almns_acudientes'},
    {'texto1':'Notas','texto2':'logros y recuperaciones','imagen':'2.png','link':'alumnos.almns_calificaciones'},
    {'texto1':'Grados','texto2':'y promociones','imagen':'5.png','link':'alumnos.almns_promocion'}]
    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Alumnos", username=session.get('username'))
