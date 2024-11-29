# Usa la imagen base de Python
FROM python:3.9-slim



# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY . /app/

# Expone el puerto en el que Flask correrá
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "run.py"]



#Agregar:
#1. ENV PYTHONDONTWRITEBYTECODE=1
#Esta configuración desactiva la escritura de archivos de bytecode (.pyc) en el sistema de archivos del contenedor.

#Detalles:
#Por defecto: Python compila automáticamente los scripts que se ejecutan en archivos de bytecode .pyc, los cuales se almacenan en directorios como __pycache__.
#Con esta configuración: Python no generará los archivos .pyc.
#Ventajas:
#Reduce el uso de espacio: Los archivos .pyc pueden acumularse y ocupar espacio innecesario.
#Evita problemas de permisos: En contenedores, los sistemas de archivos pueden ser de solo lectura o restringidos, y evitar la generación de archivos .pyc simplifica la ejecución.
#Facilita depuración: No tendrás que preocuparte por archivos compilados antiguos que puedan interferir en tu código.
#2. ENV PYTHONUNBUFFERED=1
#Esta configuración desactiva el buffering de la salida estándar (stdout) y de error (stderr).

#Detalles:
#Por defecto: Python usa buffering para mejorar el rendimiento, lo que significa que las salidas (print, logs, etc.) no se muestran inmediatamente, sino que se almacenan en un buffer y se imprimen en bloque.
#Con esta configuración: La salida de Python se imprime directamente en el terminal sin retrasos.
#Ventajas:
#Log en tiempo real: Es útil en entornos como Docker, donde necesitas ver los logs en tiempo real.
#Mejor integración: Las herramientas de orquestación (por ejemplo, Docker y Kubernetes) funcionan mejor con logs no bufferizados."""
