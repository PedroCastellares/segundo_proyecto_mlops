# LÍNEA 1: Importamos la clase LinearRegression de la librería Scikit-Learn.
# Este algoritmo busca trazar una línea recta matemática óptima que cruce entre
# los puntos de datos para aprender a predecir una variable en base a otra.
from sklearn.linear_model import LinearRegression

def entrenar_modelo_casas(df):
    """Toma la tabla de datos, aísla las variables y entrena el modelo de IA.

    Args:
        df (pd.DataFrame): Tabla estructurada con las columnas de las casas.

    Returns:
        LinearRegression: El objeto del algoritmo entrenado (el cerebro de la IA).
    """
    # LÍNEA 14: Imprimimos un mensaje de control en la consola para monitorear el flujo.
    print("\n🤖 [Modelado] Iniciando el entrenamiento del algoritmo de IA...")
    
    # LÍNEA 17: Extremos la variable predictora (X) o característica.
    # Scikit-Learn exige que las características (X) se entreguen en formato de matriz
    # bidimensional (una tabla), por eso usamos doble corchete '[["habitaciones"]]'.
    X = df[["habitaciones"]]
    
    # LÍNEA 22: Extraemos la variable objetivo (y) o la etiqueta que queremos predecir.
    # Como es una sola columna de respuestas, se entrega como un vector unidimensional (un corchete).
    y = df["precio_real"]
    
    # LÍNEA 26: Instanciamos el objeto del modelo matemático en una variable vacía.
    modelo = LinearRegression()
    
    # LÍNEA 29: El comando 'fit' es el momento donde ocurre la "magia" del Machine Learning.
    # El algoritmo analiza las parejas de (X, y) para calcular la pendiente y el intercepto.
    modelo.fit(X, y)
    
    # LÍNEA 33: Usamos '.score()' para calcular el coeficiente de determinación (R²).
    # Esta métrica matemática devuelve un valor entre 0 y 1 que indica qué tan precisa es la línea.
    # Un valor de 0.98 significa que el modelo explica el 98% de la realidad de los precios.
    precision = modelo.score(X, y)
    
    # LÍNEA 38: Imprimimos el resultado de la auditoría matemática formateado a dos decimales.
    print(f"🎯 [Modelado] ¡IA entrenada con éxito! Precisión del modelo (R²): {precision:.2f}")
    
    # LÍNEA 41: Devolvemos el objeto del modelo entrenado (el archivo binario con el conocimiento).
    return modelo
