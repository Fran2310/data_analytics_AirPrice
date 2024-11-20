from .hist_graph import gen_hist


"""
*Distribucion:
    - Los billetes de la clase economy se venden en cantidades mucho mayores que los billetes Business
"""

def graph_gen(data, colors, size=(), img=False):
    data_filtered = data[data['class'].isin(['Economy', 'Business'])]
    
    info_graph = {
        'title': 'Distribución de precios y reservas de boletos para las clases',
        'x_name': 'Precio (INR)',
        'y_name': 'N° Tickets (frecuencia)',
        'group_by': 'class',
        'x_col': 'price',
        'label_suffix': 'Clase'
    }
    
    gen_hist(data_filtered, colors, info_graph, size, img)