from flask import render_template,session
from . import colegio
from .views import *
from app.core.Mirlt import DB  # Importa la clase DB


p=('/colegio')


@colegio.route('/colegio')
def r_portal():
    # Aquí podrías obtener datos de la base de datos
    menu = [
    {'texto1': 'Docentes', 'texto2': 'y personal', 'imagen': 'docentes.png', 'link': 'colegio.docentes'},
    {'texto1': 'Decretos', 'texto2': 'legales', 'imagen': 'decretos.png', 'link': 'colegio.decretos'},
    {'texto1': 'Eventos', 'texto2': 'y actividades', 'imagen': 'eventos.png', 'link': 'colegio.eventos'}]

    # Renderiza una plantilla para mostrar los resultados
    return render_template('core/portal.html', menu=menu, username=session.get('username'))

@colegio.route(p+'/docentes')
def docentes():
    encabezados= ['--Cédula--','--Nombres--','--Apellidos--','--Cargo--','Dirección','Teléfono', 'opciones'] #DB('SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS  WHERE TABLE_NAME = "occb_profesor"  ORDER BY ORDINAL_POSITION;',username="").run_query()
    empleados=DB('SELECT  CC_NUMERO,NOMBRES,APELLIDOS,CARGO,DIRECCION,TELEFONO  FROM occb_profesor;', username="").run_query()
    return  render_template('colegio/docentes.html',encabezados=encabezados, empleados=empleados, username=session.get('username'))

@colegio.route(p+'/decretos')
def decretos():
    return  render_template('colegio/decretos.html',username=session.get('username'))

@colegio.route(p+ '/eventos')
def eventos():
    return  render_template('colegio/eventos.html',  username=session.get('username'))

@colegio.route(p+'/docentes/agregar')
def dcnt_agregar():
    return render_template('colegio/agregar.html',encabezados=[], empleados=[], username=session.get('username'))

@colegio.route(p+'/docentes/ver')
def dcnt_ver():
    return ""
'''
colegio.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('colegio/matriculas.html', resultados=resultados)
'''
