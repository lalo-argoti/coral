from flask import render_template
from . import usuario
from .views import *

@usuario.route('/config')
def r_config():
    return render_template('usuario/portal.html', titulo='Configuración', resultados=['Edita tus ajustes aquí.'])

@usuario.route('/usuario')
def r_portal():
    resultados = portal()  # Simula obtener datos
    return render_template('usuario/portal.html', titulo='Portal', resultados=resultados)



@usuario.route('/salir')
def r_salir():
    return render_template('usuario/portal.html', titulo='Salir', mensaje='Has cerrado sesión.', resultados=[])




"""
@alumnos.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('alumnos/matriculas.html', resultados=resultados)

"""
