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
