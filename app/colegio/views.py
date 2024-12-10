from flask import render_template
from app.core.Mirlt import DB  # Importa la clase DB
import logging
from datetime import datetime
def perfil(sujeto):
    # Construir la consulta SQL basada en la presencia del parámetro 'sujeto'
    if sujeto:
        query = f'''SELECT CC_NUMERO, NOMBRES, APELLIDOS, FECHA_NAC, CARGO, LUG_EXP, EST_CIVIL, LIB_MILIT, GENERO, DIRECCION, TELEFONO,  FEC_VINCUL, DECRETO, UNIVERS, CURSILLOS, NOM_GRADO1, REG_GRADO1, ESCAL_SE, email FROM  occb_profesor WHERE CC_NUMERO = {sujeto}; '''    
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
            "CC_NUMERO": row[0], "NOMBRES": row[1], "APELLIDOS": row[2],  "FECHA_NAC": row[3],  "CARGO": row[4], "LUG_EXP": row[5],
            "EST_CIVIL": row[6],  "LIB_MILIT": row[8-1],  "GENERO": row[9-1],  "DIRECCION": row[10-1],  "TELEFONO": row[11-1],
            "FEC_VINCUL": row[12-1], "DECRETO": row[13-1],  "UNIVERS": row[14-1],  "CURSILLOS": row[15-1],   "NOM_GRADO1": row[16-1], "REG_GRADO1": row[17-1],
            "ESCAL_SE": row[18-1],  "email": row[19-1], }
        profesores.append(profesor)
    # Renderizar la plantilla con los datos de los profesores
    return profesores



def levanta_la_mano(docente_id,action,nombres,apellidos,cargo,email,CC_NUMERO, session, decreto, lug_exp, est_civil, lib_milit, genero, direccion, telefono, fec_vincul, univers, cursillos, nom_grado1, reg_grado1, escal_se):

    if action == 'crear':
        # Crear un nuevo docente
        decreto = decreto if decreto else " "
        lug_exp = lug_exp if lug_exp else " "
        est_civil = est_civil if est_civil else " "
        lib_milit = lib_milit if lib_milit else " "
        genero = genero if genero else " "
        direccion = direccion if direccion else " "
        telefono = telefono if telefono else " "
        fec_vincul =  datetime.now().strftime('%Y-%m-%d')  # Formato YYYY-MM-DD fec_vincul if fec_vincul else
        univers =univers if univers else " "
        cursillos = cursillos if cursillos else " "
        nom_grado1 = nom_grado1 if nom_grado1 else " "
        reg_grado1 = reg_grado1 if reg_grado1 else " "
        escal_se = escal_se if escal_se else " "
        DB(f"""    INSERT INTO occb_profesor 
            (CC_NUMERO, NOMBRES, APELLIDOS, CARGO, LUG_EXP, EST_CIVIL, LIB_MILIT, GENERO, DIRECCION, TELEFONO, 
             FEC_VINCUL, DECRETO, UNIVERS, CURSILLOS, NOM_GRADO1, REG_GRADO1, ESCAL_SE, email) 
            VALUES 
            ({CC_NUMERO}, '{nombres}', '{apellidos}', '{cargo}', '{lug_exp}', '{est_civil}', '{lib_milit}', 
             '{genero}', '{direccion}', '{telefono}', '{fec_vincul}', '{decreto}', '{univers}', '{cursillos}', 
             '{nom_grado1}', '{reg_grado1}', '{escal_se}', '{email}')
        """, username="").run_query()

        encabezados= ['--Cédula--','--Nombres--','--Apellidos--','--Cargo--','correo-e','Teléfono', 'opciones']   
        empleados=DB('SELECT  CC_NUMERO,NOMBRES,APELLIDOS,CARGO,email,TELEFONO  FROM occb_profesor;', username="").run_query()
        return ('colegio/agregar.html', encabezados, empleados, "", ["SUCCES","Registro agregado."])

    elif action== 'ver': 
        logging.info("Pulsaron ver")
        profesores= perfil(docente_id) 
        return ('core/perfil.html', "","",profesores,["SUCCES",""])

    elif action == 'editar':
        DB(f"UPDATE occb_profesor SET NOMBRES='{nombres}', APELLIDOS='{apellidos}', CARGO='{cargo}', email='{email}' WHERE CC_NUMERO={docente_id}", username="").run_query()
        encabezados= ['--Cédula--','--Nombres--','--Apellidos--','--Cargo--','correo-e','Teléfono', 'opciones']   
        empleados=DB('SELECT  CC_NUMERO,NOMBRES,APELLIDOS,CARGO,email,TELEFONO  FROM occb_profesor;', username="").run_query()
        return ('colegio/agregar.html' , encabezados,  empleados, "",  ["DANGER","Se va a editar una persona"] )

    elif action == 'eliminar':
        logging.info("Pulsaron eliminar")
        # Eliminar un docente
        DB(f"DELETE FROM occb_profesor WHERE CC_NUMERO = {docente_id}", username="").run_query()
        encabezados= ['--Cédula--','--Nombres--','--Apellidos--','--Cargo--','correo-e','Teléfono', 'opciones']   
        empleados=DB('SELECT  CC_NUMERO,NOMBRES,APELLIDOS,CARGO,email,TELEFONO  FROM occb_profesor;', username="").run_query()
        return ('colegio/agregar.html', encabezados, empleados, "", ["DANGER","Se ha eliminado un registro"] )
  
    return "Acción no reconocida", 400
