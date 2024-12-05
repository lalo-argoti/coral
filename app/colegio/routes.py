from flask import render_template, session, request, url_for
from . import colegio
from .views import *
from app.core.Mirlt import DB  # Importa la clase DB
import logging

p=('/colegio')

@colegio.route(p+'/norma')
def norma():
    return ""

@colegio.route(p+'/docentes')
def docentes():
    encabezados= ['--Cédula--','--Nombres--','--Apellidos--','--Cargo--','correo-e','Teléfono', 'opciones'] #DB('SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS  WHERE TABLE_NAME = "occb_profesor"  ORDER BY ORDINAL_POSITION;',username="").run_query()
    empleados=DB('SELECT  CC_NUMERO,NOMBRES,APELLIDOS,CARGO,email,TELEFONO  FROM occb_profesor;', username="").run_query()
    return  render_template('colegio/docentes.html',encabezados=encabezados, empleados=empleados, username=session.get('username'))

@colegio.route(p+'/decretos')
def decretos():
     datos= DB(f"SELECT id,titulo, resumen FROM occb_decretos;", username="").run_query()   #WHERE colegio= mi_colegio
     return render_template('core/tabla.html',datos=datos, encabezados=["Título","resumen"],titulo="normatividades",link=url_for('colegio.norma') , username=session.get('username'))

@colegio.route(p+ '/eventos')
def eventos():
    return  render_template('colegio/eventos.html',  username=session.get('username'))

@colegio.route(p+'/docentes/agregar')
def dcnt_agregar():
    return render_template('colegio/agregar.html',encabezados=[], empleados=[], username=session.get('username'))

@colegio.route(p + '/docentes/ver')
def dcnt_ver():
    profesores= perfil( request.args.get('sujeto', default=None, type=int))
    return render_template('core/perfil.html', profesores=profesores, username=session.get('username'))
    
@colegio.route(p+'/docentes/guardar')
def dcnt_guardar():
    # Recibir los datos enviados desde el formulario
    datos_recibidos = request.form.to_dict()  # Convierte los datos del formulario en un diccionario

    # Llamar a la función `guardar_datos` en `views.py` y pasarle los datos
    resultado = guardar_datos(datos_recibidos)
    # Retornar una notificación según el resultado
    if resultado:
        return "Guardado exitosamente", 200
    else:
        return "Error al guardar", 500

@colegio.route(p)
def r_portal():
    menu = [
    {'texto1': 'Planta', 'texto2': 'docente', 'imagen': 'docente.png', 'link': 'colegio.docentes'},
    {'texto1': 'Normatividad', 'texto2': '', 'imagen': 'decretos.png', 'link': 'colegio.decretos'},
    {'texto1': 'Eventos', 'texto2': 'y actividades', 'imagen': 'eventos.png', 'link': 'colegio.eventos'}]
    return render_template('core/portal.html', menu=menu, username=session.get('username'))
