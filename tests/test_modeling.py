# LÍNEA 1: Importamos Pandas para fabricar una tabla de datos sintética en memoria.
import pandas as pd
# LÍNEA 3: Importamos el algoritmo base de Scikit-Learn para verificar el tipo de objeto.
from sklearn.linear_model import LinearRegression
# LÍNEA 5: Importamos la función de modelado que vamos a auditar en este examen.
from src.modeling import entrenar_modelo_casas

def test_entrenar_modelo_casas_retorna_objeto_valido_y_predice():
    """Prueba unitaria automatizada para certificar la calidad matemática de la IA."""
    
    # 1. PREPARACIÓN: Fabricamos un pequeño diccionario de datos de juguete en la RAM.
    datos_prueba = {
        "habitaciones":[1, 2, 3],
        "precio_real": [100000, 150000, 200000]
    }
    df_prueba = pd.DataFrame(datos_prueba)
    
    # 2. EJECUCIÓN: Pasamos la tabla de juguete a tu función de entrenamiento real.
    modelo_entrenado = entrenar_modelo_casas(df_prueba)
    
    # 3. AFIRMACIONES: Exigimos verdades matemáticas rigurosas.
    
    # Afirmación A: Exigimos que el objeto devuelto sea obligatoriamente una instancia de 'LinearRegression'.
    assert isinstance(modelo_entrenado, LinearRegression), "❌ Error: El módulo no devolvió un objeto de regresión válido."
    
    # Afirmación B: Verificamos si el modelo realmente aprendió y puede predecir el futuro.
    # Le pedimos que calcule el precio para una casa hipotética de 4 habitaciones.
    # '.predict()' exige una estructura de matriz, por eso usamos doble corchete '[[4]]'.
    prediccion = modelo_entrenado.predict([[4]])
    
    # Afirmación C: Exigimos que la predicción matemática devuelva un número mayor a cero.
    # Si el modelo devolviera un precio negativo o vacío, el examen fallará de inmediato.
    assert prediccion[0] > 0, f"❌ Error: El modelo calculó un precio incoherente: {prediccion[0]}"
