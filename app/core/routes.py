from flask import render_template, session
from . import core
from .views import *
from app.core.Mirlt import DB  # Importa la clase DB


@core.route('/')
def r_portal():
    titulo="Inicio"
    menu=[]
    if session.get('empresa')==130230414:
         menu=[{'texto1':'Bases de','texto2':'datos','imagen':'1.png','link':'coral.databases'}] #,
         #{'texto1':'Gestión','texto2':'y configuraciones','imagen':'1.png','link':'matriculas.mtrcls_gestion'}]
    return render_template('core/portal.html', menu=menu,  titulo=titulo ,username=session.get('username'))

