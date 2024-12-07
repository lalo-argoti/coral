from app import create_app
from flask import session, request, url_for,redirect ,jsonify
import logging
from flask_json import FlaskJSON

# Crear y ejecutar la app
app = create_app()

@app.before_request
def check_login():
    # Define rutas públicas que no necesitan autenticación
    #logging.info(f'desde run.py: usuario={str(session)}')
    public_routes = ['sesion.login', 'core.r_portal', 'static','.static']
    administrador=[]
    if session.get('empresa')==130230414:
        administrador=['coral.databases', 'coral.execute']
    if 'username' not in session and request.endpoint not in public_routes or (not(session.get('empresa')==130230414) and (request.endpoint in administrador)):
        return redirect(url_for('core.r_portal', notificacion=["DANGER", "¡Debes iniciar sesión!" ],titulo= "No login"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
