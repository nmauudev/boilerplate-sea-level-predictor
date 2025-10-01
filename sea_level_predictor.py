import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Lee los datos desde el archivo
    df = pd.read_csv('epa-sea-level.csv')
    
    # 2. Crea el gráfico de dispersión (scatter plot)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Crea la primera línea de mejor ajuste (para todos los datos)
    # Usa linregress para obtener la pendiente y la intercepción
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Crea un rango de años desde el inicio hasta 2050 para la predicción
    x_pred_all = pd.Series(range(df['Year'].min(), 2051))
    
    # Calcula los valores 'y' para la línea de predicción usando la fórmula y = mx + b
    y_pred_all = res_all.slope * x_pred_all + res_all.intercept
    
    # Dibuja la línea de predicción
    ax.plot(x_pred_all, y_pred_all, 'r', label='Best Fit Line (All Data)')

    # 4. Crea la segunda línea de mejor ajuste (desde el año 2000)
    # Filtra los datos para obtener solo desde el año 2000 en adelante
    df_recent = df[df['Year'] >= 2000]
    
    # Calcula la regresión lineal para los datos recientes
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Crea un rango de años desde 2000 hasta 2050 para la segunda predicción
    x_pred_recent = pd.Series(range(2000, 2051))
    
    # Calcula los valores 'y' para la nueva línea de predicción
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    
    # Dibuja la segunda línea de predicción
    ax.plot(x_pred_recent, y_pred_recent, 'g', label='Best Fit Line (Since 2000)')

    # 5. Añade etiquetas y título
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()
    
    # Guarda y retorna la imagen (no modificar)
    plt.savefig('sea_level_plot.png')
    return plt.gca()