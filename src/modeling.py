# LÍNEA 1: Importamos el algoritmo de Regresión Lineal de Scikit-Learn.
from sklearn.linear_model import LinearRegression
# LÍNEA 3: Importamos la librería oficial de MLflow para activar el cuaderno de bitácora científico.
import mlflow

def entrenar_modelo_casas(df):
    """Toma la tabla de datos, entrena el algoritmo y registra la ciencia en la base de datos SQLite."""
    print("\n🤖 [Modelado] Iniciando el entrenamiento y registro indexado en SQLite...")
    
    # LÍNEA 9: Le indicamos a MLflow la ruta exacta de nuestra base de datos relacional SQLite.
    # El prefijo 'sqlite:///' le ordena crear un archivo único sólido llamado 'mlflow.db' en la raíz de tu carpeta.
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    
    # LÍNEA 13: Seleccionamos el experimento sanado con rutas universales
    mlflow.set_experiment("Proyecto_Casas_Fijo")
    
    # LÍNEA 16: Separamos las variables (X: característica, y: objetivo) como en la Unidad 2.
    X = df[["habitaciones"]]
    y = df["precio_real"]
    
    # LÍNEA 20: El comando 'start_run' abre una nueva línea de registro (un experimento individual).
    # Usamos la cláusula 'with' para que si el código falla, la bitácora se cierre de forma segura en el disco.
    with mlflow.start_run(run_name="Modelo_Base_Regresion"):
        
        # LÍNEA 24: Instanciamos y entrenamos el algoritmo matemático de Scikit-Learn.
        modelo = LinearRegression()
        modelo.fit(X, y)
        precision = modelo.score(X, y)
        
        # LÍNEA 29: REGISTRO DE PARÁMETROS (La configuración inicial de la IA).
        # Guardamos en la base de datos que este modelo calculó su propio punto de partida (intercepto).
        mlflow.log_param("fit_intercept", True)
        
        # LÍNEA 33: REGISTRO DE MÉTRICAS (El rendimiento final obtenido).
        # Guardamos la puntuación de precisión R² lograda por la línea matemática.
        mlflow.log_metric("r2_score", precision)
        
        # LÍNEA 37: REGISTRO DE ARTEFACTOS (El archivo binario del cerebro del modelo).
        # Guarda el objeto de Python empaquetado para que pueda ser consumido en el futuro.
        mlflow.sklearn.log_model(modelo, artifact_path="modelo_final_casas")
        
        print(f"🎯 [Modelado] ¡IA entrenada y guardada en la DB! Precisión (R²): {precision:.2f}")
        
    return modelo

