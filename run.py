from app import create_app
from flask import session, request, url_for,redirect


# Crear y ejecutar la app
app = create_app()


@app.before_request
def check_login():
    # Define rutas públicas que no necesitan autenticación
    public_routes = ['sesion.login', 'core.r_portal', 'static', '.static']
    if ('username' not in session and request.endpoint not in public_routes):
        return redirect(url_for('core.r_portal'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
