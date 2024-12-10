from flask import render_template,session, jsonify, request, url_for
from . import coral
from .views import *
import logging
from app.core.Mirlt import DB  # Importa la clase DB
import ast
@coral.route('/coral')
def r_portal():

    menu = [
    {'texto1': 'Consultas', 'texto2': 'sql', 'imagen': 'distribucion.png', 'link': 'coral.databases'},
    {'texto1': 'Tablas de la', 'texto2': 'base de datos', 'imagen': 'logros.png', 'link': 'coral.tablas'},
    {'texto1': 'Grupos de ', 'texto2': 'usuarios', 'imagen': 'evaluaciones.png', 'link': 'user_group.user_group'}
    ]
    return render_template('core/portal.html', menu=menu,  username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))




@coral.route('/coral/databases')
def databases():
    return render_template('coral/databases.html', username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

@coral.route('/coral/databases/tablas')
def tablas():
     datos, encabezados=mostrarTablas()
     return render_template('core/tabla.html',datos=datos, encabezados=encabezados,titulo="tablas", link2=True,  username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

@coral.route('/coral/databases/copia')
def r_copia():
    mensaje= copia()
    return mensaje

@coral.route('/coral/databases/tabla/<string:ref>')
def datos(ref):
     encabezados,datos= renderTabla(ref)
     return render_template('core/tabla.html',datos=datos, encabezados=encabezados,titulo=ref,link=url_for('coral.tablas') , username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

@coral.route('/coral/user_grupoOLD')
def user_group ():
    # Simulación de datos de la base de datos
    vectores=DB('SELECT * FROM occb_user_group', username="").run_query()
    columnas = ["id", "nombre", "permisos", "proyecto", "usado"]
    grupos= [dict(zip(columnas, fila)) for fila in vectores]
    '''grupos = [
        {"id": 1, "nombre": "Administradores", "permisos": '["create", "read", "update", "delete"]', "proyecto": "Proyecto A", "usado": 1},
        {"id": 2, "nombre": "Usuarios Básicos", "permisos": '["read"]', "proyecto": "Proyecto B", "usado": 0}
    ]'''
    campos = [
        ["nombre", "char 16"], 
        ["permisos", "text"], 
        ["proyecto", "char 64"], 
        ["usado", "int"]
    ]
    return render_template('coral/admin_grupos.html', grupos=grupos, campos=campos, username=session.get('username'),menu_data =  ast.literal_eval(session['menu']))

# Ruta para procesar consultas SQL
# Ruta para procesar consultas SQL
@coral.route('/execute', methods=['POST'])
def execute_query():
    try:
        # Obtiene la consulta SQL desde el frontend
        query = request.form.get('query')
        logging.info(f'Query recibido desde el frontend: {query}')
        
        # Ejecuta la consulta en la base de datos
        respuesta = DB(query=query, username=session.get('id_user')).run_query()
        logging.info(f'Respuesta del manejador de base de datos: {respuesta}')
        
        # Retorna respuesta de éxito
        return jsonify({'success': True, 'message': 'Consulta ejecutada con éxito.', 'result': respuesta})
    except Exception as e:
        # Registra el error en el log
        logging.error(f'Error ejecutando la consulta: {str(e)}')
        # Retorna una respuesta con el error
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})
