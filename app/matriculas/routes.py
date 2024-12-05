#{{'texto1':'','texto2':'','imagen':'','link':''}}
from flask import render_template,session, redirect,url_for
from . import matriculas
from .views import *
import json
p=('/matriculas')

@matriculas.route(p+'/handle_actions', methods=['POST'])
def almns_handle_actions():
    alumno=request.form.get('carnet')
    action = request.form.get('action')
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    identidad = request.form.get('identidad')
    genero=request.form.get('genero')
    tipo_doc=  request.form.get('tipo_doc')
    tipo_sangre= request.form.get('tipo_sangre')
    fecha_nacimiento = request.form.get('fecha_nacimiento')
    action = request.form.get('action')

    if action == 'matricular':
        # Crear un diccionario con los datos del formulario
        student_data = {
            "codigo":alumno,"colegio":"22312", "nombres": nombres, "apellidos": apellidos, "tipo_doc":tipo_doc,
            "genero":genero, "identidad": identidad, "fecha_nacimiento": fecha_nacimiento,"tipo_sangre":tipo_sangre
        }
        process_student_data(student_data)
        return redirect(url_for('matriculas.mtrcls_inscribir', alumno=alumno))
    return "Acción no reconocida", 400

@matriculas.route(p + '/inscribir/', defaults={'alumno': None})
@matriculas.route(p+'/inscribir/<string:alumno>')
def mtrcls_inscribir(alumno):
    resultados,alumno = inscribir(alumno)
    return render_template('matriculas/inscribir.html', resultados=resultados,alumno =alumno, username=session.get('username'))

@matriculas.route(p+'/lista')
def mtrcls_lista():
    datos,encabezados= listaEstudiantes()
    return render_template('core/tabla2.html', datos= datos, link2=True, encabezados=encabezados ,titulo="estudiantes", username=session.get('username'))

@matriculas.route(p+'/gestion')
def mtrcls_gestion():
    return render_template('matriculas/gestion', username=session.get('username'))

@matriculas.route('/matriculas')
def r_portal():
    itemsMenu =[{'texto1':'Lista de','texto2':'estudiantes','imagen':'listaEst.png','link':'matriculas.mtrcls_lista'},
    {'texto1':'Matriculas','texto2':'e inscripciones','imagen':'2.png','link':'matriculas.mtrcls_inscribir'},
    {'texto1':'Gestión','texto2':'y configuraciones','imagen':'1.png','link':'matriculas.mtrcls_gestion'}]
    return render_template('core/portal.html', menu=itemsMenu, titulo= "Matrículas", username=session.get('username'))
