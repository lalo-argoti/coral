from flask import render_template,session
from . import materias
from .views import *

@materias.route('/materias/logros')
def logros():
     datos= DB(f"SELECT id,CODIGO, SIGLA, FRASE  FROM occb_CCI_fras;", username="").run_query()   #WHERE colegio= mi_colegio
     return render_template('core/tabla.html',datos=datos, encabezados=["","",""],titulo="frases",link="#" , username=session.get('username'))

@materias.route('/materias/evaluaciones')
def evaluaciones():
   return ""
    
@materias.route('/materias')
def r_portal():
    menu = [
    {'texto1': 'Distribución', 'texto2': 'de horarios', 'imagen': 'distribucion.png', 'link': 'grupos.distribucion'},
    {'texto1': 'Logros', 'texto2': 'académicos', 'imagen': 'logros.png', 'link': 'materias.logros'},
    {'texto1': 'Evaluaciones', 'texto2': 'y calificaciones', 'imagen': 'evaluaciones.png', 'link': 'materias.evaluaciones'}
    ]
    return render_template('core/portal.html', menu=menu,  username=session.get('username'))
