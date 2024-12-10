from flask import render_template, session, request, url_for
from . import colegio
from .views import *
from app.core.Mirlt import DB  # Importa la clase DB
import logging
from datetime import datetime
import ast
p=('/colegio')

@colegio.route(p+'/norma')
def norma():
    return ""

##////////DOCENTES //////////////////////////
q="/docentes"
@colegio.route(p+'/docentes')
def docentes():
    encabezados= ['--Cédula--','--Nombres--','--Apellidos--','--Cargo--','correo-e','Teléfono', 'opciones']   
    empleados=DB('SELECT  CC_NUMERO,NOMBRES,APELLIDOS,CARGO,email,TELEFONO  FROM occb_profesor;', username="").run_query()
    return  render_template('colegio/docentes.html',encabezados=encabezados, empleados=empleados, username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

@colegio.route(p+'/docentes/agregar')
def dcnt_agregar():
    encabezados= ['--Cédula--','--Nombres--','--Apellidos--','--Cargo--','correo-e','Teléfono', 'opciones']   
    empleados=DB('SELECT  CC_NUMERO,NOMBRES,APELLIDOS,CARGO,email,TELEFONO  FROM occb_profesor;', username="").run_query()
    campos=[
    {"name": "CC_NUMERO", "type": "number", "label": "CC Número", "required": True},
    {"name": "NOMBRES", "type": "text", "label": "Nombres", "required": True},
    {"name": "APELLIDOS", "type": "text", "label": "Apellidos", "required": True},
    {"name": "FECHA_NAC", "type": "date", "label": "Fecha de Nacimiento", "required": False},
    {"name": "CARGO", "type": "text", "label": "Cargo", "required": True},
    {"name": "LUG_EXP", "type": "text", "label": "Lugar de Expedición", "required": False},
    {"name": "EST_CIVIL", "type": "text", "label": "Estado Civil", "required": False},
    {"name": "LIB_MILIT", "type": "text", "label": "Libreta Militar", "required": False},
    {"name": "GENERO", "type": "text", "label": "Género", "required": True},
    {"name": "DIRECCION", "type": "text", "label": "Dirección", "required": True},
    {"name": "TELEFONO", "type": "tel", "label": "Teléfono", "required": False},
    {"name": "FEC_VINCUL", "type": "date", "label": "Fecha de Vinculación", "required": False},
    {"name": "DECRETO", "type": "text", "label": "Decreto", "required": False},
    {"name": "UNIVERS", "type": "text", "label": "Universidad", "required": False},
    {"name": "CURSILLOS", "type": "text", "label": "Cursillos", "required": False},
    {"name": "NOM_GRADO1", "type": "text", "label": "Nombre del Grado 1", "required": False},
    {"name": "REG_GRADO1", "type": "text", "label": "Registro del Grado 1", "required": False},
    {"name": "ESCAL_SE", "type": "text", "label": "Escalafón", "required": False},
    {"name": "email", "type": "email", "label": "Email", "required": True},
    ]
    return render_template('colegio/agregar.html',campos=campos, empleados=empleados, username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))



@colegio.route(p + '/handle_docente_actions', methods=['POST'])
def handle_docente_actions():
    docente_id = request.form.get('docente_id')
    action = request.form.get('action')
    nombres = request.form.get('NOMBRES')
    apellidos = request.form.get('APELLIDOS')
    cargo = request.form.get('CARGO')
    email = request.form.get('email')
    CC_NUMERO = request.form.get('CC_NUMERO')
    decreto = request.form.get('DECRETO')  # Ahora en mayúsculas
    lug_exp = request.form.get('LUG_EXP')
    est_civil = request.form.get('EST_CIVIL')
    lib_milit = request.form.get('LIB_MILIT')
    genero = request.form.get('GENERO')
    direccion = request.form.get('DIRECCION')
    telefono = request.form.get('TELEFONO')
    fec_vincul = request.form.get('FEC_VINCUL')
    univers = request.form.get('UNIVERS')
    cursillos = request.form.get('CURSILLOS')
    nom_grado1 = request.form.get('NOM_GRADO1')
    reg_grado1 = request.form.get('REG_GRADO1')
    escal_se = request.form.get('ESCAL_SE')  # Ahora en mayúsculas

    x=levanta_la_mano(docente_id,action,nombres,apellidos,
             cargo,email,CC_NUMERO, session,decreto, lug_exp, est_civil, lib_milit, genero, 
             direccion, telefono, fec_vincul, univers, cursillos, nom_grado1, reg_grado1, escal_se) #views.py

    return render_template(x[0], encabezados=x[1], empleados=x[2], profesores= x[3],notificacion=x[4], username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

# Ruta para mostrar la lista de docentes
@colegio.route(p + '/admin_docentes')
def admin_docentes():
    # Consultamos los docentes de la base de datos
    vectores = DB('SELECT * FROM occb_profesor;', username="").run_query()
    columnas = ["CC_NUMERO", "NOMBRES", "APELLIDOS", "CARGO", "email"]
    docentes = [dict(zip(columnas, fila)) for fila in vectores]
    return render_template('colegio/admin_docentes.html', docentes=docentes, username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

@colegio.route(p+'/decretos')
def decretos():
     datos= DB(f"SELECT id,titulo, resumen FROM occb_decretos;", username="").run_query()   #WHERE colegio= mi_colegio
     return render_template('core/tabla.html',datos=datos, encabezados=["Título","resumen"], titulo="normatividades", link=url_for('colegio.norma') , username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

@colegio.route(p+ '/eventos')
def eventos():
    return  render_template('colegio/eventos.html',  username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

@colegio.route(p)
def r_portal():
    menu = [
    {'texto1': 'Planta', 'texto2': 'docente', 'imagen': 'docente.png', 'link': 'colegio.docentes'},
    {'texto1': 'Normatividad', 'texto2': '', 'imagen': 'decretos.png', 'link': 'colegio.decretos'},
    {'texto1': 'Eventos', 'texto2': 'y actividades', 'imagen': 'eventos.png', 'link': 'colegio.eventos'}]
    return render_template('core/portal.html', menu=menu, username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))
      
