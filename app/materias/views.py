from app.core.Mirlt import DB  # Importa la clase DB

# views.py
def portal():
    # Crea una instancia de la clase DB
    #consulta = DB(query="SELECT * FROM tabla_ejemplo", username="admin")
    
    # Ejecuta un método de la clase DB
    #resultados = consulta.run_query()

    resultado =DB(query=f"SELECT * FROM occb_fras;", username="").run_query()
    return resultado

def get_examen_data():
    query_examen = "SELECT * FROM occb_examen WHERE id = 1"
    query_preguntas = '''SELECT p.pregunta, p.respuesta_correcta, p.respuestas_incorrectas, p.tipo_de_multimedia, p.ruta_al_archivo_en_flask, r.porcentaje
        FROM occb_exmn_pregunta p
        JOIN occb_exmn_prgnt_relacion r ON p.id = r.pregunta_id
        WHERE r.examen_id = 1
    '''
    
    examen = DB(query_examen, username="").run_query()
    preguntas = DB(query_preguntas,username="").run_query()
    preguntas2=[]
    for pregunta in preguntas:
       x= eval(pregunta[2])
       preguntas2.append([pregunta[0],pregunta[1],[*x],pregunta[3],pregunta[4],pregunta[5]])
    return {
        "examen": examen[0],
        "preguntas": preguntas2
    }

