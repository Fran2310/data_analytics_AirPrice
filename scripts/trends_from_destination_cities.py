from .bar_graph_3C import gen_bar_3C


"""
*Observacion:
    - La ruta de Chennai a Bangalore es la más costosa
    - La ciudad de Delhi ofrece los precios más bajos
"""

def graph_gen(data, colors, size=(), img=False):

    #Genera un gráfico de barras para el precio promedio por ciudad de destino, 
    #considerando la ciudad de origen como categoría (hue)

    # DataFrame con precios promedio agrupados por ciudad de destino y origen
    data_graph = data.groupby(['destination_city', 'source_city'])['price'].mean().reset_index()
    
    info_graph = {
        'title': 'Precio medio del Boleto por ciudad de destino',
        'x_name': 'Ciudad de Destino',
        'y_name': 'Precio Promedio (INR)',
        'legend': 'Ciudad de origen',
        'x_col': 'destination_city',
        'y_col': 'price',
        'hue_col': 'source_city'
    }
    
    gen_bar_3C(data_graph, colors, info_graph, size, img)
