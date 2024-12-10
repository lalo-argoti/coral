from flask import render_template, session, request, url_for
from . import buscar
from .views import *
from app.core.Mirlt import DB  # Clase DB para las consultas

@buscar.route('/buscar')
def r_portal():
    query = request.args.get('query', '').strip()
    resultados = []

    if query:
        # Búsqueda en estudiantes
        # Buscamos por nombres o apellidos que contengan el término
        sql_estudiantes = f"SELECT codigo, nombres, apellidos, doc_ident FROM occb_estudiantes WHERE nombres LIKE '%{query}%' OR apellidos LIKE '%{query}%'"
        data_estudiantes = DB(query=sql_estudiantes, username=session.get('id_user')).run_query()

        # Añadimos estos resultados a la lista, asumiendo que la URL relevante es la lista de matrículas
        for row in data_estudiantes:
            # row[0] = codigo, row[1] = nombres, row[2] = apellidos
            nombre_completo = f"{row[1]} {row[2]}"
            resultados.append({
                'title': f"Estudiante: {nombre_completo}",
                'url': url_for('matriculas.mtrcls_lista'),  # Podrías crear una URL específica que muestre detalles del alumno
                'score': 10  # Asignamos un score alto a resultados de estudiantes por ejemplo
            })

        # Aquí podrías agregar más búsquedas en otras tablas, por ejemplo en docentes:
        sql_docentes = f"SELECT CC_NUMERO, NOMBRES, APELLIDOS FROM occb_profesor WHERE NOMBRES LIKE '%{query}%' OR APELLIDOS LIKE '%{query}%'"
        data_docentes = DB(query=sql_docentes, username=session.get('id_user')).run_query()
        for row in data_docentes:
            doc_name = f"{row[1]} {row[2]}"
            resultados.append({
                'title': f"Docente: {doc_name}",
                'url': url_for('colegio.docentes'),
                'score': 8
            })

        # Búsqueda en noticias:
        sql_noticias = f"SELECT id, title FROM occb_noticias WHERE title LIKE '%{query}%' OR noticia LIKE '%{query}%'"
        data_noticias = DB(query=sql_noticias, username=session.get('id_user')).run_query()
        for row in data_noticias:
            resultados.append({
                'title': f"Noticia: {row[1]}",
                'url': url_for('colegio.eventos'), # Podrías tener una URL específica para la noticia
                'score': 5
            })

        # Aquí puedes agregar más búsquedas en otras tablas (occb_articulo, occb_decretos, etc.)
        # y asignar scores diferentes según su relevancia.

        # Ordenar resultados por el campo 'score' (relevancia), mayor a menor
        resultados = sorted(resultados, key=lambda x: x['score'], reverse=True)

    return render_template('buscar/portal.html', resultados=resultados, username=session.get('username'))
