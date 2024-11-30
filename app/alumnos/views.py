from app.core.Mirlt import DB  # Importa la clase DB

# views.py
def portal():
    # Crea una instancia de la clase DB
    #consulta = DB(query="SELECT * FROM tabla_ejemplo", username="admin")

    # Ejecuta un método de la clase DB
    #resultados = consulta.run_query()
    resultado = DB(query=f"SELECT * FROM occb_user;", username="").run_query()  #["hola mundo"]
    if resultado :
        return resultado[0]
    else :
        return ""


def matriculas():
     return ("")

def acudientes():
  return ""

def calificaciones():
  return ""

def promocion():
  return ""

def guardar_alumno():
   return ""

import json

def process_student_data(student_data):
    # Imprimir los datos en consola para verificar
    #DB(query = "--Procesando estudiante:"+str( student_data),username="").run_query()

    return ""
