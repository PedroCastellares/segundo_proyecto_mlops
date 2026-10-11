# LÍNEA 1: Importamos la librería Pandas, que es el estándar de la industria
# para manipular, limpiar y analizar datos estructurados en forma de tablas (DataFrames).
import pandas as pd

def cargar_datos_casas():
    """Realiza la ingesta de datos leyendo el dataset físico desde el disco.

    Returns:
        pd.DataFrame: Una tabla estructurada de Pandas con los datos de las casas.
    """
    # LÍNEA 10: Definimos en una variable la ruta relativa donde vive nuestro archivo CSV.
    # El punto de partida de esta ruta siempre es la raíz de tu proyecto.
    ruta_dataset = "data/datos_casas.csv"
    
    # LÍNEA 14: Imprimimos un mensaje en la terminal para rastrear en vivo el flujo del pipeline.
    print(f"📥 [Ingesta] Buscando y abriendo el archivo en: {ruta_dataset}...")
    
    # LÍNEA 17: Usamos la función nativa de Pandas '.read_csv()' para abrir el archivo físico.
    # Esta función transforma el texto separado por comas del CSV en un objeto DataFrame (tabla).
    df_casas = pd.read_csv(ruta_dataset)
    
    # LÍNEA 21: Usamos la función integrada 'len()' de Python para contar las filas cargadas.
    # Esto nos sirve como una auditoría rápida para saber si el archivo se leyó completo.
    print(f"✅ [Ingesta] Éxito. Se cargaron {len(df_casas)} registros en la memoria RAM.")
    
    # LÍNEA 25: Devolvemos la tabla de datos lista para ser consumida por las siguientes etapas.
    return df_casas
