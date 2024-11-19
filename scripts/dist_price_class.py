from .hist_graph import gen_hist

def graph_gen(data, colors, size=(), img=False):
    data_filtered = data[data['class'].isin(['Economy', 'Business'])]
    
    info_graph = {
        'title': 'Distribución de precios de billetes para clase business y clase económica',
        'x_name': 'Precio (INR)',
        'y_name': 'N° Tickets (frecuencia)',
        'group_by': 'class',
        'x_col': 'price',
        'label_suffix': 'Clase'
    }
    
    gen_hist(data_filtered, colors, info_graph, size, img)