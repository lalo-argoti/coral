from app.core.Mirlt import DB  # Importa la clase DB
from datetime import datetime

def guardar_profesor(datos):
    datos_docente = {
        "CC_NUMERO": 12345,  # ID del docente
        "NOMBRES": "",
        "APELLIDOS": "Pérez",
        "CARGO": "",
        "LUG_EXP": "",
        "EST_CIVIL": "Soltero",
        "LIB_MILIT": "",
        "GENERO": "",
        "DIRECCION": "Calle 123",
        "TELEFONO": "3001234567",
        "FEC_VINCUL": "",
        "DECRETO": "1234-ABC",
        "UNIVERS": "Universidad Nacional",
        "CURSILLOS": "",
        "NOM_GRADO1": "",
        "REG_GRADO1": "",
        "ESCAL_SE": "",
        "email": "profesor@example.com"
    }

    # Asignar valores predeterminados
    datos_docente["NOMBRES"] = datos_docente["NOMBRES"].strip() or "0"
    datos_docente["CARGO"] = datos_docente["CARGO"].strip() or "0"
    datos_docente["LUG_EXP"] = datos_docente["LUG_EXP"].strip() or "0"
    datos_docente["LIB_MILIT"] = datos_docente["LIB_MILIT"].strip() or "0"
    datos_docente["GENERO"] = datos_docente["GENERO"].strip() or "0"
    datos_docente["FEC_VINCUL"] = datos_docente["FEC_VINCUL"].strip() or datetime.now().strftime("%Y-%m-%d")
    datos_docente["CURSILLOS"] = datos_docente["CURSILLOS"].strip() or "0"
    datos_docente["NOM_GRADO1"] = datos_docente["NOM_GRADO1"].strip() or "0"
    datos_docente["REG_GRADO1"] = datos_docente["REG_GRADO1"].strip() or "0"
    datos_docente["ESCAL_SE"] = datos_docente["ESCAL_SE"].strip() or "0"

    # Construir la consulta SQL
    query = f"""UPDATE occb_profesor
        SET 
            NOMBRES = '{datos_docente["NOMBRES"]}', 
            APELLIDOS = '{datos_docente["APELLIDOS"]}', 
            CARGO = '{datos_docente["CARGO"]}', 
            LUG_EXP = '{datos_docente["LUG_EXP"]}', 
            EST_CIVIL = '{datos_docente["EST_CIVIL"]}', 
            LIB_MILIT = '{datos_docente["LIB_MILIT"]}', 
            GENERO = '{datos_docente["GENERO"]}', 
            DIRECCION = '{datos_docente["DIRECCION"]}', 
            TELEFONO = '{datos_docente["TELEFONO"]}', 
            FEC_VINCUL = '{datos_docente["FEC_VINCUL"]}', 
            DECRETO = '{datos_docente["DECRETO"]}', 
            UNIVERS = '{datos_docente["UNIVERS"]}', 
            CURSILLOS = '{datos_docente["CURSILLOS"]}', 
            NOM_GRADO1 = '{datos_docente["NOM_GRADO1"]}', 
            REG_GRADO1 = '{datos_docente["REG_GRADO1"]}', 
            ESCAL_SE = '{datos_docente["ESCAL_SE"]}', 
            email = '{datos_docente["email"]}'
        WHERE CC_NUMERO = {datos_docente["CC_NUMERO"]} ;"""

    # Ejecutar la consulta
    DB(query, username="").run_query()
    
