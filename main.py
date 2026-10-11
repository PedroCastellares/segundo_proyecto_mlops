# LÍNEA 1: Importamos la librería 'os' (Operating System) del núcleo de Python.
# Nos permite interactuar con el sistema de archivos de tu laptop HP Spectre.
import os

# LÍNEA 5: Importamos la librería 'sys' (System) del núcleo de Python.
# Nos da acceso a variables y funciones que interactúan directamente con el intérprete.
import sys

# LÍNEA 9: Una línea crítica de MLOps. Tomamos la ruta absoluta de la carpeta actual donde
# se está ejecutando este archivo y la agregamos al mapa de búsqueda de Python ('sys.path').
# Esto garantiza que Python pueda encontrar tus módulos sin importar desde dónde lances el comando.
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# LÍNEA 14: Importamos la función de carga de datos desde tu módulo independiente 'ingestion'.
from src.ingestion import cargar_datos_casas

# LÍNEA 17: Importamos la función de entrenamiento desde tu módulo independiente 'modeling'.
from src.modeling import entrenar_modelo_casas

def ejecutar_pipeline_completo():
    """Coordina y ejecuta de inicio a fin todas las etapas del pipeline de MLOps."""
    print("🚀 === INICIANDO PIPELINE END-TO-END DE MLOps ===")
    
    # LÍNEA 24: ETAPA 1 - Ingestión de datos.
    # Llamamos a tu función modular. Ella va al disco, lee el CSV y nos devuelve la tabla estructurada.
    datos_casas = cargar_datos_casas()
    
    # LÍNEA 28: ETAPA 2 - Entrenamiento del Modelo de IA.
    # Tomamos la tabla que nos devolvió la Etapa 1 y se la pasamos en bandeja de plata al entrenador.
    # El algoritmo calcula la regresión lineal y nos devuelve el objeto del cerebro matemático entrenado.
    modelo_final = entrenar_modelo_casas(datos_casas)
    
    print("🚀 === PIPELINE EJECUTADO CON ÉXITO EN TU SISTEMA ===\n")
    
    # Devolvemos el modelo final listo por si se necesita consumir en producción
    return modelo_final

# LÍNEA 38: La cláusula estándar de protección de Python. Garantiza que este script
# solo se ejecute si tú lo lanzas directamente, y no si otra librería intenta importarlo.
if __name__ == "__main__":
    ejecutar_pipeline_completo()
