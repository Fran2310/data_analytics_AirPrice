import matplotlib.pyplot as plt

"""
* Distrubucion:
    - La mayor parte de los boletos, tanto para reservas hechas 1 día antes como 2 días antes de la salida, se concentran en el rango de precios bajos de aproximadamente 10,000 a 20,000 INR. Este rango representa la mayor frecuencia en el histograma
    - A medida que el precio aumenta (más allá de los 30,000 INR), la frecuencia de boletos reservados disminuye significativamente
    - La mayoría de las reservas realizadas 1 o 2 días antes de la salida se encuentran en rangos de precios similares, lo que indica que los boletos no se encarecen significativamente
    - El gran volumen de reservas en el rango de precios bajos sugiere que los clientes que reservan con poca antelación priorizan boletos económicos
"""


def graph_gen(data, colors, size=(), img=False):
    data_filtered = data[data['days_left'].isin([1, 2])]

    info_graph = {
        'title': 'Distribución de precios de boletos para 1 y 2 días antes de la salida',
        'x_name': 'Precio (INR)',
        'y_name': 'N° Tickets (frecuencia)'
    }
    
    gen_hist(data_filtered, colors, info_graph, size, img)

def gen_hist(data, colors, info_graph, size, img):
    if size:
        plt.figure(figsize=size)

    color_map = {1: colors[0], 2: colors[6]}

    for days, group_data in data.groupby('days_left'):
        plt.hist(group_data['price'], bins=30, alpha=0.5, label=f'{days} Días Antes', color=color_map[days])

    plt.title(info_graph['title'])
    plt.xlabel(info_graph['x_name'])
    plt.ylabel(info_graph['y_name'])
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()

    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()
