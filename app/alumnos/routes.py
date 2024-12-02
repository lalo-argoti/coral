from flask import render_template, request, redirect, url_for,session
from . import alumnos
from .views import *

p='/alumnos'

@alumnos.route(p)
def r_portal():
   # Aquí podrías obtener datos de la base de datos
    itemsMenu =[{'texto1':'Matriculas','texto2':'e inscripciones','imagen':'3.png','link':'matriculas.r_portal'},
    {'texto1':'Acudientes','texto2':'y contacto','imagen':'6.png','link':'alumnos.almns_acudientes'},
    {'texto1':'Notas','texto2':'logros y recuperaciones','imagen':'2.png','link':'alumnos.almns_calificaciones'},
    {'texto1':'Grados','texto2':'y promociones','imagen':'5.png','link':'alumnos.almns_promocion'}]
    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Alumnos", username=session.get('username'))

@alumnos.route(p+'/acudientes')
def almns_acudientes():
    # Aquí podrías obtener datos de la base de datos
    resultados = acudientes()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/acudientes.html', resultados=resultados, username=session.get('username'))

@alumnos.route(p+'/calificaciones')
def almns_calificaciones():
    # Aquí podrías obtener datos de la base de datos
    DB(query=f'--accion: calificaciones', username="").run_query()

    resultados = calificaciones()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/calificaciones.html', resultados=resultados, username=session.get('username'))

@alumnos.route(p+'/promocion')
def almns_promocion():
    # Aquí podrías obtener datos de la base de datos
    resultados = promocion()
    DB(query="-- desde promocion", username="").run_query()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/promocion.html', resultados=resultados , username=session.get('username'))


@alumnos.route(p+'/handle_actions', methods=['POST'])
def almns_handle_actions(): 
    
    # Obtener datos del formulario
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    identidad = request.form.get('identidad')
    fecha_nacimiento = request.form.get('fecha_nacimiento')
    action = request.form.get('action')
    #DB(query="--"+nombres+action , username="").run_query()
    # Validar la acción seleccionada
    if action == 'matricular':
        # Crear un diccionario con los datos del formulario
        student_data = {
            "nombres": nombres,
            "apellidos": apellidos,
            "identidad": identidad,
            "fecha_nacimiento": fecha_nacimiento
        }

        # Procesar los datos en views.py
        process_student_data(student_data)

        # Redirigir a otra página (por ejemplo, el portal del colegio)
        return redirect(url_for('matriculas.mtrcls_inscribir')+"#")

    # Si la acción no coincide con las esperadas
    return "Acción no reconocida", 400
