from app.core.Mirlt import DB  # Importa la clase DB

def perfil(sujeto):
    # Construir la consulta SQL basada en la presencia del parámetro 'sujeto'
    if sujeto:
        query = f'''SELECT CC_NUMERO, NOMBRES, APELLIDOS, FECHA_NAC, CARGO, LUG_EXP, EST_CIVIL, CC_LUGAR, LIB_MILIT, GENERO, DIRECCION, TELEFONO,  FEC_VINCUL, DECRETO, UNIVERS, CURSILLOS, NOM_GRADO1, REG_GRADO1, ESCAL_SE, email FROM  occb_profesor WHERE CC_NUMERO = {sujeto}; '''    
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
            "EST_CIVIL": row[6],  "CC_LUGAR": row[7],  "LIB_MILIT": row[8],  "GENERO": row[9],  "DIRECCION": row[10],  "TELEFONO": row[11],
            "FEC_VINCUL": row[12], "DECRETO": row[13],  "UNIVERS": row[14],  "CURSILLOS": row[15],   "NOM_GRADO1": row[16], "REG_GRADO1": row[17],
            "ESCAL_SE": row[18],  "email": row[19], }
        profesores.append(profesor)
    # Renderizar la plantilla con los datos de los profesores
    return profesores
