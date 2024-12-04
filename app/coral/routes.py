from flask import render_template,session, jsonify, request, url_for
from . import coral
from .views import *
import logging
from app.core.Mirlt import DB  # Importa la clase DB


@coral.route('/coral')
def r_portal():
    # Aquí podrías obtener datos de la base de datos
    resultados = portal()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('coral/portal.html', resultados=resultados,  username=session.get('username'))


@coral.route('/databases')
def databases():
    # Aquí podrías obtener datos de la base de datos
    # Renderiza una plantilla para mostrar los resultados
    return render_template('coral/databases.html', username=session.get('username'))

@coral.route('/tablas')
def tablas():
     encabezados=["Tabla", ""]
     datos= DB("SHOW TABLES;", username="").run_query()
     return render_template('core/tabla.html',datos=datos, encabezados=encabezados,titulo="tablas",link2= "url_for('coral.datos',datos=eval(datos[0]))",  username=session.get('username'))


@coral.route('/tablas/datos/<string:datos>')
def datos(datos):
     c_encabezados=  DB(f"DESCRIBE {datos};", username="").run_query()
     encabezados=  [columna[0] for columna in c_encabezados]
     datos= DB(f"SELECT * FROM {datos};", username="").run_query()
     return render_template('core/tabla.html',datos=datos, encabezados=encabezados,titulo=f"{datos}",link=url_for('coral.datos') , username=session.get('username'))

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
