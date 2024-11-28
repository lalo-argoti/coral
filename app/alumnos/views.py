from app.core.Mirlt import DB  # Importa la clase DB

# views.py
def obtener_lista_alumnos():
    # Crea una instancia de la clase DB
    consulta = DB(query="SELECT * FROM tabla_ejemplo", username="admin")

    # Ejecuta un método de la clase DB
    resultados = consulta.run_query()
    return resultado
