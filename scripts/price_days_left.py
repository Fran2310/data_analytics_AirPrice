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
        'title': 'Precio Promedio de Boletos Según Días de Antelación',
        'x_name': 'Días de Antelación',
        'y_name': 'Precio Promedio del Boleto',
        'x_data': avg_prices.index,
        'y_data': avg_prices.values,
        'xticks_step': 2  #mostrar cada 2 etiquetas en el eje X
    }
    
    gen_line(info_graph, colors, size, img)

def gen_line(info_graph, colors, size, img):
    if size:
        plt.figure(figsize=size)

    plt.plot(info_graph['x_data'], info_graph['y_data'], marker='o', color=colors[1])

    xticks = range(0, len(info_graph['x_data']), info_graph['xticks_step'])
    plt.xticks(xticks, info_graph['x_data'][xticks], rotation=45)
    plt.title(info_graph['title'])
    plt.xlabel(info_graph['x_name'])
    plt.ylabel(info_graph['y_name'])
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()
