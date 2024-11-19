from .hist_graph import gen_hist

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
        'y_name': 'N° Tickets (frecuencia)',
        'group_by': 'days_left',
        'x_col': 'price',
        'label_suffix': 'Días Antes'
    }
    
    gen_hist(data_filtered, colors, info_graph, size, img)





