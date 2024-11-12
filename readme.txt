# Instrucciones para ejecutar la aplicación Flask

1. Clona el repositorio en tu máquina local:
   git clone <URL del repositorio>

2. Navega al directorio de la aplicación:
   cd my_flask_app

3. (Opcional) Si no tienes Docker instalado, puedes instalarlo desde: https://www.docker.com/get-started

4. Para ejecutar la aplicación sin Docker, instala las dependencias:
   pip install -r requirements.txt

5. Inicia la aplicación con el siguiente comando:
   python run.py

6. La aplicación debería estar disponible en http://127.0.0.1:5000/.

# Para ejecutar la aplicación con Docker:

1. Construye la imagen de Docker:
   docker build -t my_flask_app .

2. Ejecuta el contenedor:
   docker run -p 5000:5000 my_flask_app

3. La aplicación estará accesible en http://localhost:5000/.
