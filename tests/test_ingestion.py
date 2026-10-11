# LÍNEA 1: Importamos la librería Pandas para poder usar sus tipos de datos de control.
import pandas as pd

# LÍNEA 4: Importamos la función de ingesta que queremos auditar en este examen.
from src.ingestion import cargar_datos_casas

def test_cargar_datos_casas_retorna_dataframe_valido():
    """Prueba unitaria automatizada para verificar la estructura y calidad de la ingesta."""
    
    # 1. EJECUCIÓN (Llamamos a la función real bajo un entorno de prueba controlado)
    df_resultado = cargar_datos_casas()
    
    # 2. AFIRMACIONES (Usamos la palabra clave 'assert' para exigir verdades matemáticas)
    
    # Afirmación A: Exigimos que el objeto resultante sea obligatoriamente una tabla (DataFrame) de Pandas.
    # Si la función devolviera un archivo de texto o una lista vacía, el test se romperá de inmediato.
    assert isinstance(df_resultado, pd.DataFrame), "❌ Error: La ingesta no devolvió una tabla de Pandas."
    
    # Afirmación B: Exigimos que la tabla contenga exactamente las 5 filas físicas de tu archivo CSV.
    assert len(df_resultado) == 5, f"❌ Error: Se esperaban 5 registros, pero se contaron {len(df_resultado)}."
    
    # Afirmación C: Exigimos que la columna 'habitaciones' exista dentro de la estructura de la tabla.
    assert "habitaciones" in df_resultado.columns, "❌ Error: La columna 'habitaciones' desapareció del dataset."
