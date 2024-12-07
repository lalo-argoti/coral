from app.core.Mirlt import DB  # Importa la clase DB

from flask import render_template,session,request, jsonify
#from models import db, UserGroup  # Importa el modelo correspondiente
from . import user_group
from .views import *

p= "/coral/user_grupo"

@user_group.route(p + '/handle_actions', methods=['POST'])
def handle_user_group_actions():
    user_group_id = request.form.get('user_group_id')
    action = request.form.get('action')
    nombre = request.form.get('name')
    permission= request.form.get('permission')
    proyecto = request.form.get('proyecto')
    usado = request.form.get('usado')
    id_g= request.form.get('id_g')
    if action == 'crear':
        # Aquí se crearán los datos en la base de datos
        DB(f"INSERT INTO occb_user_group (`user_group_id`, `name`, `permission`, `proyecto`, `usado`) VALUES ({id_g},'{nombre}','{permission}','{proyecto}','{usado}')",username="").run_query()
        return "Grupo creado", 201
    elif action == 'editar':
        return jsonify({"success": True, "message": "Editar"})

        # Aquí se editarán los datos en la base de datos
        #return render_template('user_group/admin_grupos.html', Grupo_x_ver=user_group_id ,grupos=grupos, campos=campos, username=session.get('username'))    
        #DB("DELETE FROM occb_user_group WHERE occb_user_group ={user_group_id};", username="").run_query()
    elif action == 'eliminar':
        # Aquí se eliminará en la base de datos
        DB(f"DELETE FROM occb_user_group WHERE user_group_id = '{user_group_id}';", username="").run_query()
        return jsonify({"succes":True, "message":"Grupo eliminado"})
    return "Acción no reconocida", 400


@user_group.route(p+'/user_grupo')
def user_group ():
    # Simulación de datos de la base de datos
    vectores=DB('SELECT * FROM occb_user_group;', username="").run_query()
    columnas = ["id", "nombre", "permisos", "proyecto", "usado"]
    grupos= [dict(zip(columnas, fila)) for fila in vectores]
    '''grupos = [
        {"id": 1, "nombre": "Administradores", "permisos": '["create", "read", "update", "delete"]', "proyecto": "Proyecto A", "usado": 1},
        {"id": 2, "nombre": "Usuarios Básicos", "permisos": '["read"]', "proyecto": "Proyecto B", "usado": 0}
    ]'''
    campos = [
        ["id", "int"],
        ["nombre", "char 16"], 
        ["permisos", "text"], 
        ["proyecto", "char 64"], 
        ["usado", "int"]
    ]
    return render_template('user_group/admin_grupos.html', grupos=grupos, campos=campos, username=session.get('username'))    
