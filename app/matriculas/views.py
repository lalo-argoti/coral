from app.core.Mirlt import DB  # Importa la clase DB
from flask import request
def portal():
 return ""

# views.py
def process_student_data(student_data):
    #{'nombres': 'we', 'apellidos': 'we', 'identidad': 'we', 'fecha_nacimiento': '2099-12-12'}
    x=DB('SELECT IFNULL(MAX(codigo), 0) + 1 AS nuevo_codigo FROM occb_estudiantes;', username="" ).run_query()[0][0]
    # agregar colegio  "colegio"
    DB(f'''INSERT INTO occb_estudiantes (codigo ,nombres, 	apellidos, 	tipo_doc, 	doc_ident, 	genero, 	fecha_nac, 	TIPO_SANGRE)
    values ({student_data['codigo']}, "{student_data['nombres']}","{student_data['apellidos']}","{student_data['tipo_doc']}","{student_data['identidad']}",
    "{student_data['genero']}","{student_data['fecha_nacimiento']}","{student_data['tipo_sangre']}");''', username="").run_query()
    return ("Se ha guardado el estudiante")

