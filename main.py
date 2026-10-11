import os
import sys

# Agregamos la ruta absoluta al mapa de búsqueda de Python
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importamos nuestros módulos y la librería oficial de MLflow
from src.ingestion import cargar_datos_casas
from src.modeling import entrenar_modelo_casas
import mlflow

def ejecutar_pipeline_completo():
    print("🚀 === INICIANDO PIPELINE END-TO-END DE MLOps ===")
    
    # LÍNEA 15: Conectamos el orquestador a la misma base de datos SQLite
    mlflow.set_tracking_uri("sqlite:///mlflow.db")

    # ETAPA 1: Ingestión de datos
    datos_casas = cargar_datos_casas()
    
    # ETAPA 2: Entrenamiento del Modelo de IA y registro automático
    modelo_final = entrenar_modelo_casas(datos_casas)
    
    # ETAPA 3: Consulta automática de la bitácora indexada en SQLite
    print("\n📊 === CONSULTANDO LA BASE DE DATOS CIENTÍFICA EN VIVO ===")
    
    # Usamos la API de MLflow para buscar todas las corridas registradas en la DB
    runs = mlflow.search_runs(experiment_names=["Proyecto_Prediccion_Casas"])
    
    print("\n-------------------------------------------------------------")
    print(" NOMBRE DEL RUN              | PARÁMETRO (Intercept) | MÉTRICA (R²)")
    print("-------------------------------------------------------------")
    # Recorremos cada fila que nos devolvió la consulta SQL interna de MLflow
    for _, fila in runs.iterrows():
        nombre = fila["tags.mlflow.runName"]
        parametro = fila["params.fit_intercept"]
        metrica = fila["metrics.r2_score"]
        print(f" {nombre:<26} | {parametro:<21} | {metrica:.2f}")
    print("-------------------------------------------------------------")
    
    print("🚀 === PIPELINE EJECUTADO CON ÉXITO EN TU SISTEMA ===\n")


if __name__ == "__main__":
    ejecutar_pipeline_completo()
