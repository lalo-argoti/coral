from flask import render_template
from . import matriculas
from .views import *

@matriculas.route('/matriculas')
def r_portal():
    # Aquí podrías obtener datos de la base de datos
    resultados = portal()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('matriculas/portal.html', resultados=resultados)


@matriculas.route('/handle_actions', methods=['POST'])
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
        return redirect(url_for('#'))

    # Si la acción no coincide con las esperadas
    return "Acción no reconocida", 400



@matriculas.route('/inscribir')
def mtrcls_inscribir():
    # Aquí podrías obtener datos de la base de datos
    resultados = ""
    # Renderiza una plantilla para mostrar los resultados
    return render_template('matriculas/inscribir.html', resultados=resultados)

@matriculas.route('/gestion')
def mtrcls_gestion():
    # Aquí podrías obtener datos de la base de datos
    resultados = ""
    # Renderiza una plantilla para mostrar los resultados
    return render_template('matriculas/gestion.html', resultados=resultados)

