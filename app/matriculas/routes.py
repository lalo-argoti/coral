#{{'texto1':'','texto2':'','imagen':'','link':''}}
from flask import render_template,session, redirect,url_for
from . import matriculas
from .views import *
import json
p=('/matriculas')
@matriculas.route('/matriculas')
def r_portal():
    # Aquí podrías obtener datos de la base de datos
    itemsMenu =[{'texto1':'Lista de','texto2':'estudiantes','imagen':'listaEst.png','link':'matriculas.mtrcls_lista'},
    {'texto1':'Matriculas','texto2':'e inscripciones','imagen':'2.png','link':'matriculas.mtrcls_inscribir'},
    {'texto1':'Gestión','texto2':'y configuraciones','imagen':'1.png','link':'matriculas.mtrcls_gestion'}]
    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Matrículas", username=session.get('username'))

@matriculas.route(p+'/handle_actions', methods=['POST'])
def almns_handle_actions():
    alumno=request.form.get('carnet')
    action = request.form.get('action')
    # Obtener datos del formulario
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    identidad = request.form.get('identidad')
    genero=request.form.get('genero')
    tipo_doc=  request.form.get('tipo_doc')
    tipo_sangre= request.form.get('tipo_sangre')
    fecha_nacimiento = request.form.get('fecha_nacimiento')
    action = request.form.get('action')
    #DB(query="--"+nombres+action , username="").run_query()
    # Validar la acción seleccionada
    if action == 'matricular':
        # Crear un diccionario con los datos del formulario
        student_data = {
            "codigo":alumno,
            "colegio":"22312",
            "nombres": nombres,
            "apellidos": apellidos,
            "tipo_doc":tipo_doc,
            "genero":genero,
            "identidad": identidad,
            "fecha_nacimiento": fecha_nacimiento,
            "tipo_sangre":tipo_sangre

        }
        # Procesar los datos en views.py
        process_student_data(student_data)
        # Redirigir a otra página (por ejemplo, el portal del colegio)
        return redirect(url_for('matriculas.mtrcls_inscribir', alumno=alumno))
    # Si la acción no coincide con las esperadas
    return "Acción no reconocida", 400

@matriculas.route(p + '/inscribir/', defaults={'alumno': None})
@matriculas.route(p+'/inscribir/<string:alumno>')
def mtrcls_inscribir(alumno):
    # Aquí podrías obtener datos de la base de datosç
    resultados=[]
    if alumno is None:
      alumno=DB('SELECT IFNULL(MAX(codigo), 0) + 1 AS nuevo_codigo FROM occb_estudiantes;', username="" ).run_query()[0][0]

    else:
      resultados=DB(f"SELECT * FROM occb_estudiantes WHERE codigo={alumno}", username="").run_query()[0]
      # Renderiza una plantilla para mostrar los resultados
      return render_template('matriculas/inscribir.html', resultados=resultados,alumno =alumno, username=session.get('username'))
    return render_template('matriculas/inscribir.html', resultados=resultados,alumno =alumno, username=session.get('username'))

@matriculas.route(p+'/lista')
def mtrcls_lista():
    # Aquí podrías obtener datos de la base de datos
    resultados = ""
    datos=DB("SELECT * FROM occb_estudiantes;", username="").run_query()
    datos= [
        [url_for('matriculas.mtrcls_inscribir', alumno=t[0])] + list(t)        for t in datos
    ]

    encabezados=["carnet","nombres","apellidos","T","documento","género","nacimiento","RH","grupo"]
    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/tabla2.html', datos= datos, link2=True, encabezados=encabezados ,titulo="estudiantes", username=session.get('username'))

@matriculas.route(p+'/gestion')
def mtrcls_gestion():
    return render_template('matriculas/gestion', username=session.get('username'))
