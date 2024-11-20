import pandas as pd
from .bar_graph import gen_bar
import matplotlib.pyplot as plt
import seaborn as sns

def graph_gen_stops(data, colors, size=(), img=False):
    """
    Genera una gráfica de barras que muestra la influencia de las paradas en el precio promedio.
    """
    # Calcular precio promedio por cantidad de paradas
    data_graph = data.groupby('stops')['price'].mean()

    # Ajustar el orden lógico de las categorías
    stop_order = ['zero', 'one', 'two_or_more']
    data_graph = data_graph.reindex(stop_order)

    # Configurar información del gráfico
    info_graph = {
        'title': 'Influencia de las Paradas en el Precio del Vuelo',
        'x_name': 'Cantidad de Paradas',
        'y_name': 'Precio Promedio (INR)',
        'x_data': None,  # No aplica para Series
        'y_data': None   # No aplica para Series
    }

    # Usar gen_bar para generar el gráfico
    gen_bar(data_graph, colors, info_graph, size, img)

def graph_gen_duration(data, colors, size=(), img=False):
    """
    Genera una gráfica de barras que muestra la influencia de las paradas en la duración promedio.
    """
    # Calcular duración promedio por cantidad de paradas
    data_graph = data.groupby('stops')['duration'].mean()

    # Ajustar el orden lógico de las categorías
    stop_order = ['zero', 'one', 'two_or_more']
    data_graph = data_graph.reindex(stop_order)

    # Configurar información del gráfico
    info_graph = {
        'title': 'Influencia de las Paradas en la Duración del Vuelo',
        'x_name': 'Cantidad de Paradas',
        'y_name': 'Duración Promedio (Horas)',
        'x_data': None,  # No aplica para Series
        'y_data': None   # No aplica para Series
    }

    # Usar gen_bar para generar el gráfico
    gen_bar(data_graph, colors, info_graph, size, img)

