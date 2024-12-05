from app.core.Mirlt import DB  # Importa la clase DB

# views.py
def portal():
    # Crea una instancia de la clase DB
    #consulta = DB(query="SELECT * FROM tabla_ejemplo", username="admin")

    # Ejecuta un método de la clase DB
    #resultados = consulta.run_query()

    resultado = ["hola mundo"]
    return resultado



def copia():

 # Obtener el listado de las tablas en la base de datos
 tablas=DB(query="SHOW TABLES", username="").run_query()

 # Crear el archivo de informe
 with open('informe.txt', 'w') as f:
    for tabla in tablas:

        tabla_nombre = tabla[0]
        
        # Escribir el nombre de la base de datos y la tabla
        f.write(f"basededatos/{tabla_nombre}\n")
        
        # Obtener la descripción de las columnas (nombre, tipo de dato, etc.)
        columnas=DB(query=f"DESCRIBE {tabla_nombre}",username="").run_query()
        
        
        for columna in columnas:
            campo = columna[0]
            tipo = columna[1]
            nulo = columna[2]
            clave = columna[3]
            predeterminado = columna[4]
            extra = columna[5]
            
            # Formatear el tipo de dato y otros detalles
            campo_info = f"  {campo} {tipo}"
            
            if "auto_increment" in extra:
                campo_info += " auto_increment"
            
            if clave == "PRI":
                campo_info += " key"
            
            # Escribir la información de la columna
            f.write(f"{campo_info}\n")
        
        # Agregar una línea en blanco para separar las tablas
        f.write("\n")

 # Cerrar la conexión a la base de datos
 #cursor.close()
 #db.close()

 return ("Informe generado exitosamente en informe.txt.")

