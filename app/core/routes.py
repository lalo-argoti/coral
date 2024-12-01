from flask import render_template, session
from . import core
from .views import *
from app.core.Mirlt import DB  # Importa la clase DB


@core.route('/')
def r_portal():
    titulo="Inicio"
    menu=[]
    return render_template('core/portal.html', menu=menu,  titulo=titulo ,username=session.get('username'))

