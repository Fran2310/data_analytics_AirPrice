import pandas as pd
from .bar_graph import gen_bar
from .bar_graph_3C import gen_bar_3C


"""
Influencia de las paradas en los precios del boleto por clase

-Se nota un aumento significativo en el precio del boleto cuando los vuelos se lleva a cabo 1 o mas paradas, esto debido a los gastos operativos que conlleva como tarifas aeroportuarias, 
comida y suministros para los pasajeros, checkeos que aumenten el tiempo de espera y otras cosas haciendo que el precio aumente para suplir estas perdidas.

"""

"""
DEPRECATED: EL VALOR DEL PRECIO ESTABA SESGADO POR LA DIFERENCIA DE PRECIOS DE CLASE
def graph_gen_stops(data, colors, size=(), img=False):
    
    #Genera una gráfica de barras que muestra la influencia de las paradas en el precio promedio.
    
    # Calcular precio promedio por cantidad de paradas
    data_graph = data.groupby('stops')['price'].mean()

    stop_order = ['zero', 'one', 'two_or_more']
    data_graph = data_graph.reindex(stop_order)

    info_graph = {
        'title': 'Influencia de las Paradas en el Precio del Vuelo',
        'x_name': 'Cantidad de Paradas',
        'y_name': 'Precio Promedio (INR)',
        'x_data': None,  # No aplica para Series
        'y_data': None   # No aplica para Series
    }

    gen_bar(data_graph, colors, info_graph, size, img)
"""

def graph_gen_stops(data, colors, size=(), img=False):
    
    #Genera una gráfica de barras que muestra la influencia de las paradas en el precio promedio
    #Se hace por clase (Economy y Business) para evitar el sesgo del precio promedio por influencia 
    #de mayor cantidad de data en la clase Economy
    
    # Calc el precio promedio por cantidad de paradas y clase
    data_graph = data.groupby(['stops', 'class'])['price'].mean().reset_index()

    # Ajustar el orden lógico de las categorías
    stop_order = ['cero', 'uno', 'dos o más']
    data_graph['stops'] = pd.Categorical(data_graph['stops'], categories=stop_order, ordered=True)
    data_graph = data_graph.sort_values(by='stops')

    info_graph = {
        'title': 'Influencia de las Paradas en el Precio del Vuelo por Clase',
        'x_name': 'Cantidad de Paradas',
        'y_name': 'Precio Promedio (INR)',
        'x_col': 'stops',  # el eje X es la cantidad de paradas
        'y_col': 'price',  # El eje Y es el precio
        'hue_col': 'class', # El hue es la clase de vuelo (Economy y Business)
        'legend': 'Clase'
    }

    gen_bar_3C(data_graph, colors, info_graph, size, img)

def graph_gen_duration(data, colors, size=(), img=False):
    
    #Genera una gráfica de barras que muestra la influencia de las paradas en la duración promedio.
    
    # Calc duración promedio por cantidad de paradas
    data_graph = data.groupby('stops')['duration'].mean()

    # Ajustar el orden lógico de las categorías
    stop_order = ['cero', 'uno', 'dos o más']
    data_graph = data_graph.reindex(stop_order)

    info_graph = {
        'title': 'Influencia de las Paradas en la Duración del Vuelo',
        'x_name': 'Cantidad de Paradas',
        'y_name': 'Duración Promedio (Horas)'
    }

    # Usar gen_bar para generar el gráfico
    gen_bar(data_graph, colors, info_graph, size, img)








