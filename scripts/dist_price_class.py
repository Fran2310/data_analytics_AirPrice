from .hist_graph import gen_hist


"""
Distribución por Clase:
- Los boletos de clase Economy tienen un rango de precios menor, concentrándose entre 0 y 20,000 INR, con un pico muy pronunciado alrededor de los 5,000 INR.
- Los boletos de clase Business se distribuyen en un rango de precios más alto, con una mayor densidad entre 40,000 y 70,000 INR.

Rangos de Precios:
- Economy: Precio máximo registrado de aproximadamente 20,000 INR, con una predominancia en los 10,000 INR.
- Business: Precio máximo registrado de aproximadamente 120,000 INR, con una predominancia entre 40,000 y 70,000 INR.
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