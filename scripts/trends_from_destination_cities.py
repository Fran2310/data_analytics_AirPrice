from .bar_graph_3C import gen_bar_3C


"""
*Observacion:
    - La ruta de Chennai a Bangalore es la más costosaS

Precio medio del boleto por ciudad de destino (Business)

    -Hyderabad en la mayoría de los casos muestra un mínimo menor costo del boleto hacia las principales ciudades de destino con respecto a las demás

    -Delhi es la segunda ciudad con los boletos mas baratos con respecto a los destinos 

    -Kolkata es la ciudad con los boletos mas caros con respecto a los destinos

Precio medio del boleto por ciudad de destino (Economy)

    -Hyderabad en la mayoría de los casos muestra un mínimo menor costo del boleto hacia las principales ciudades de destino con respecto a las demás

    -Delhi es la segunda ciudad con los boletos mas baratos 

    -Kolkata es la ciudad con los boletos mas caros de todas las ciudades

"""
"""

DEPRECATED: VALOR SE SESGO DE PRECIO
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
"""

#Genera dos gráficos de barras para el precio promedio por ciudad de destino,
#separados por clase (Economy y Business), considerando la ciudad de origen como categoría (hue).

def graph_gen_economy(data, colors, size=(), img=False): 

    # Filtrar por clase Economy
    data_economy = data[data['class'] == 'Economy']
    data_graph_economy = data_economy.groupby(['destination_city', 'source_city'])['price'].mean().reset_index()
    
    info_graph_economy = {
        'title': 'Precio Medio del Boleto por Ciudad de Destino (Economy)',
        'x_name': 'Ciudad de Destino',
        'y_name': 'Precio Promedio (INR)',
        'legend': 'Ciudad de Origen',
        'x_col': 'destination_city',
        'y_col': 'price',
        'hue_col': 'source_city'
    }

    gen_bar_3C(data_graph_economy, colors, info_graph_economy, size, img)

def graph_gen_business(data, colors, size=(), img=False): 
    
    # Filtrar por clase Business
    data_business = data[data['class'] == 'Business']
    data_graph_business = data_business.groupby(['destination_city', 'source_city'])['price'].mean().reset_index()
    
    info_graph_business = {
        'title': 'Precio Medio del Boleto por Ciudad de Destino (Business)',
        'x_name': 'Ciudad de Destino',
        'y_name': 'Precio Promedio (INR)',
        'legend': 'Ciudad de Origen',
        'x_col': 'destination_city',
        'y_col': 'price',
        'hue_col': 'source_city'
    }

    gen_bar_3C(data_graph_business, colors, info_graph_business, size, img)
