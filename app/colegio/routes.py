from flask import render_template, session, request
from . import colegio
from .views import *
from app.core.Mirlt import DB  # Importa la clase DB
import logging

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
    encabezados= ['--Cédula--','--Nombres--','--Apellidos--','--Cargo--','correo-e','Teléfono', 'opciones'] #DB('SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS  WHERE TABLE_NAME = "occb_profesor"  ORDER BY ORDINAL_POSITION;',username="").run_query()
    empleados=DB('SELECT  CC_NUMERO,NOMBRES,APELLIDOS,CARGO,email,TELEFONO  FROM occb_profesor;', username="").run_query()
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

@colegio.route(p + '/docentes/ver')
def dcnt_ver():
    # Obtener el parámetro 'sujeto' de la URL
    sujeto = request.args.get('sujeto', default=None, type=int)

    # Construir la consulta SQL basada en la presencia del parámetro 'sujeto'
    if sujeto:
        query = f''' SELECT 
                CC_NUMERO, NOMBRES, APELLIDOS, FECHA_NAC, CARGO, LUG_EXP, 
                EST_CIVIL, CC_LUGAR, LIB_MILIT, GENERO, DIRECCION, TELEFONO, 
                FEC_VINCUL, DECRETO, UNIVERS, CURSILLOS, NOM_GRADO1, REG_GRADO1, 
                ESCAL_SE, email
            FROM 
                occb_profesor
            WHERE
                CC_NUMERO = {sujeto};
        '''    

    # Ejecutar la consulta utilizando tu clase DB
    try:
        empleados = DB(query=query, username="").run_query()  # Asegúrate de pasar el username si es necesario
        print(empleados)
    except Exception as e:
        logging.error(f'Error al ejecutar la consulta: {e}')
        empleados = []

    # Mapea los resultados a una lista de diccionarios para facilitar el acceso en la plantilla
    profesores = []
    for row in empleados:
        profesor = {
            "CC_NUMERO": row[0],
            "NOMBRES": row[1],
            "APELLIDOS": row[2],
            "FECHA_NAC": row[3],
            "CARGO": row[4],
            "LUG_EXP": row[5],
            "EST_CIVIL": row[6],
            "CC_LUGAR": row[7],
            "LIB_MILIT": row[8],
            "GENERO": row[9],
            "DIRECCION": row[10],
            "TELEFONO": row[11],
            "FEC_VINCUL": row[12],
            "DECRETO": row[13],
            "UNIVERS": row[14],
            "CURSILLOS": row[15],
            "NOM_GRADO1": row[16],
            "REG_GRADO1": row[17],
            "ESCAL_SE": row[18],
            "email": row[19],
        }
        profesores.append(profesor)

    # Renderizar la plantilla con los datos de los profesores
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

'''
colegio.route('/matriculas')
def almns_matriculas():
    # Aquí podrías obtener datos de la base de datos
    resultados = matriculas()
    # Renderiza una plantilla para mostrar los resultados
    return render_template('colegio/matriculas.html', resultados=resultados)
'''
