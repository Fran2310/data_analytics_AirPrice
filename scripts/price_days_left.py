import pandas as pd
import matplotlib.pyplot as plt

"""
* Distribucion:
    - La tendencia general es que a mayor antelacion reservan su boleto, pueden encontrar precios mas bajos
    - Cuando quedan menos de 18 dias para la salida del vuelo se observa el principal aumento de precios
    - Cuando reservan a 18 dias o mas para la salida del vuelo el precio no parece aumentar significativamente, pero lo mejor es reversar con la mayor antelacion
    
"""


def graph_gen(data, colors, size=(), img=False):
    max_days_left = data['days_left'].max()
    bins = range(0, max_days_left + 3, 3)
    labels = [f'{i}-{i+2}' for i in bins[:-1]]  #crear etiquetas de los intervalos
    
    #agrupar los datos por intervalos y calcular el precio promedio
    data['days_left_bins'] = pd.cut(data['days_left'], bins=bins, labels=labels, right=False)
    avg_prices = data.groupby('days_left_bins')['price'].mean()

    info_graph = {
        'title': 'Precio Medio de Boletos Según Días de Antelación',
        'x_name': 'Días de Antelación',
        'y_name': 'Precio Medio del Boleto',
        'x_data': avg_prices.index,
        'y_data': avg_prices.values,
        'xticks_step': 2  #mostrar cada 2 etiquetas en el eje X
    }
    
    gen_line(info_graph, colors, size, img)

def gen_line(info_graph, colors, size, img):
    if size:
        plt.figure(figsize=size)

    plt.plot(info_graph['x_data'], info_graph['y_data'], marker='o', color=colors[7])

    xticks = range(0, len(info_graph['x_data']), info_graph['xticks_step'])
    plt.xticks(xticks, info_graph['x_data'][xticks], rotation=45, fontsize=10, color='#353535')
    plt.yticks(fontsize=10, color='#353535')
    plt.title(info_graph['title'], fontsize=12, fontweight='bold', color='#353535')
    plt.xlabel(info_graph['x_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.ylabel(info_graph['y_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()

def graph_gen_3line(data, colors, size=(), img=False):
    """
    Prepara los datos para el gráfico de líneas y llama a la función de graficar.
    
    data: DataFrame con la información.
    colors: Lista de colores para las líneas.
    size: Tamaño del gráfico.
    img: Booleano para guardar la gráfica como imagen.
    """
    max_days_left = data['days_left'].max()
    bins = range(0, max_days_left + 3, 3)
    labels = [f'{i}-{i+2}' for i in bins[:-1]]  # Crear etiquetas de los intervalos
    
    # Crear columna de intervalos
    data['days_left_bins'] = pd.cut(data['days_left'], bins=bins, labels=labels, right=False)

    # Filtrar datos para cada clase
    economy_data = data[data['class'] == 'Economy']
    business_data = data[data['class'] == 'Business']
    
    # Calcular precios promedio por intervalos para cada clase y general
    avg_prices_economy = economy_data.groupby('days_left_bins')['price'].mean()
    avg_prices_business = business_data.groupby('days_left_bins')['price'].mean()
    avg_prices_general = data.groupby('days_left_bins')['price'].mean()

    # Crear diccionario con datos para graficar
    info_graph = {
        'economy': avg_prices_economy,
        'business': avg_prices_business,
        'general': avg_prices_general,
        'labels': labels,  # Etiquetas comunes para el eje X
        'title': 'Precio Medio Por Clase de Boletos Según Días de Antelación',
        'x_name': 'Días de Antelación',
        'y_name': 'Precio Medio del Boleto'
    }
    
    # Llamar a la función de graficar
    gen_line_3line(info_graph, colors, size, img)

def gen_line_3line(info_graph, colors, size=(), img=False):
    """
    Genera un gráfico de líneas a partir de la información preparada.
    
    info_graph: Diccionario con datos para Economy, Business y General.
    colors: Lista de colores para las líneas.
    size: Tamaño de la gráfica.
    img: Booleano para guardar la gráfica como imagen.
    """
    if size:
        plt.figure(figsize=size)

    # Graficar cada línea
    plt.plot(info_graph['economy'].index, info_graph['economy'].values, 
            marker='s', label='Economy', color=colors[0])
    plt.plot(info_graph['business'].index, info_graph['business'].values, 
            marker='D', label='Business', color=colors[4])
    plt.plot(info_graph['general'].index, info_graph['general'].values, 
            marker='o', label='Promedio General', color=colors[7])

    # Configuración del gráfico
    plt.title(info_graph['title'], fontsize=12, fontweight='bold', color='#353535')
    plt.xlabel(info_graph['x_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.ylabel(info_graph['y_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.xticks(range(0, len(info_graph['labels']), 2), info_graph['labels'][::2], 
                rotation=45, fontsize=10, color='#353535')
    plt.yticks(fontsize=10, color='#353535')
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()

    # Guardar o mostrar
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()

