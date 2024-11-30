from flask import render_template, request, redirect, url_for,session
from . import alumnos
from .views import *

@alumnos.route('/alumnos')
def r_portal():
    
    # Aquí podrías obtener datos de la base de datos
    resultados = portal()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/portal.html', resultados=resultados, username=session.get('username') )


@alumnos.route('/matriculasv0')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/matriculas.html', resultados=resultados,  username=session.get('username'))

@alumnos.route('/acudientes')
def almns_acudientes():
    # Aquí podrías obtener datos de la base de datos
    resultados = acudientes()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/acudientes.html', resultados=resultados, username=session.get('username'))

@alumnos.route('/calificaciones')
def almns_calificaciones():
    # Aquí podrías obtener datos de la base de datos
    DB(query=f'--accion: calificaciones', username="").run_query()

    resultados = calificaciones()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/calificaciones.html', resultados=resultados, username=session.get('username'))

@alumnos.route('/promocion')
def almns_promocion():
    # Aquí podrías obtener datos de la base de datos
    resultados = promocion()
    DB(query="-- desde promocion", username="").run_query()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/promocion.html', resultados=resultados , username=session.get('username'))


@alumnos.route('/handle_actions', methods=['POST'])
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
        return redirect(url_for('alumnos.almns_matriculas')+"#")

    # Si la acción no coincide con las esperadas
    return "Acción no reconocida", 400
