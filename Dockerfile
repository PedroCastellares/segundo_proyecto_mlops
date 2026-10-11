# LÍNEA 1: Descargamos una imagen oficial de Linux ligera con Python 3.12 preinstalado.
FROM python:3.12-slim

# LÍNEA 4: Creamos y nos mudamos a una carpeta interna dentro del contenedor llamada '/app'.
WORKDIR /app

# LÍNEA 7: Copiamos tu archivo de receta de requisitos al interior del contenedor.
COPY requirements.txt .

# LÍNEA 10: Le ordenamos a la máquina Linux instalar todas las librerías científicas del proyecto.
RUN pip install --no-cache-dir -r requirements.txt

# LÍNEA 13: Copiamos absolutamente todo el código de tu proyecto local hacia el contenedor.
COPY . .

# LÍNEA 16: Desactivamos el bloqueo de archivos de MLflow para entornos virtualizados.
ENV MLFLOW_ALLOW_FILE_STORE=true

# LÍNEA 19: Exponemos el puerto 5000 para abrir una ventana de comunicación con el exterior.
EXPOSE 5000

# LÍNEA 22: La orden final. Cuando el contenedor despierte, levantará el servidor web limpio.
CMD ["mlflow", "server", "--backend-store-uri", "sqlite:///mlflow.db", "--default-artifact-root", "./mlruns", "--host", "0.0.0.0", "--port", "5000"]
