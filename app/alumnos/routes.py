from flask import render_template
from . import alumnos

@alumnos.route('/alumnos')
def lista_alumnos():
    # Llama a la función que obtiene los datos
    datos_alumnos = obtener_lista_alumnos()
    return render_template('alumnos/lista_alumnos.html', alumnos=datos_alumnos)



