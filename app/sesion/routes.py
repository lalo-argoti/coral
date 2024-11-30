from flask import render_template, request, session, redirect, url_for
from . import sesion
from .views import *
from app.core.Mirlt import DB  # Importa la clase DB


@sesion.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Consulta a la base de datos para verificar las credenciales
        query = f'SELECT * FROM occb_user WHERE username = "{username}" AND password = "{password}"'
        result=DB(query=query, username="").run_query()
        # Verificar si se encontró algún registro
        if result:
            # Si la consulta devuelve resultados, asignar el mensaje desde la base de datos
            mensaje = str(result[0][1])  # Esto asume que el mensaje está en la segunda columna
            session['username'] = result[0][2]
            session['id_user']= result[0][0]
            # Aquí también podrías redirigir al home si las credenciales son correctas
            return redirect(url_for('core.r_portal',mensaje="Conexion-exitosa"))  # Redirigir al home si el login es correcto
        else:
            # Si no se encuentra el usuario o las credenciales no coinciden
            mensaje = "Credenciales incorrectas."
            session['username']=0
    # Renderizar el template con el mensaje
    return render_template('sesion/login.html', mensaje=mensaje, error=["red",mensaje])


"""
@alumnos.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/matriculas.html', resultados=resultados)

"""
