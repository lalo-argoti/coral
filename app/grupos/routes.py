from flask import render_template,session
from . import grupos
from .views import *
from app.core.Mirlt import DB  # Importa la clase DB

@grupos.route('/grupos')
def r_portal():
   # Aquí podrías obtener datos de la base de datos
    itemsMenu =[{'texto1':'Cursos,','texto2':'materias y logros','imagen':'materias.png','link':'materias.r_portal'},
    {'texto1':'Grupos','texto2':'y clubes','imagen':'grupos.png','link':'grupos.distribucion'},
    {'texto1':'Sedes','texto2':'-','imagen':'sede.png','link':'grupos.sedes'}]
    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Grupos y materias", username=session.get('username'))

@grupos.route('/distribucion')
def distribucion():
    datos=DB("SELECT id, SEDE, CURSO, NOMBRE, JORNADA, DURAHORA FROM cursos WHERE colegio= 22312 ORDER BY CURSO;", username= "").run_query() 
    return render_template('grupos/distribucion.html', encabezados=["sede", "id", "curso","jornada", "duracion", "opciones"],datos= datos,  username=session.get('username'))

@grupos.route('/sedes')
def sedes():
    # Aquí podrías obtener datos de la base de datos
    # Renderiza una plantilla para mostrar los resultados
    return render_template('grupos/sedes.html', menu=[] , username=session.get('username'))


@grupos.route('/grupos/agregar')
def grupo_agregar():
   return "Progarmas aqui para agregar un grupo"


@grupos.route('/grupos/ver/<string:grupo>')
def grupo_ver(grupo):
   return  render_template('grupos/ver.html', titulo=f"Detalles de grupo {grupo}", username=session.get('username'))

