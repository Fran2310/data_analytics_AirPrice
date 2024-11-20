import pandas as pd
from .bar_graph import gen_bar
from .bar_graph_3C import gen_bar_3C

"""
Se observa que:

* Variaciones de precios:
    - Vistara y Air India tienen los precios promedio de boletos más altos
    - SpiceJet, GO FIRST, Indigo, y AirAsia tienen precios promedio significativamente más bajos

* Competencia:
    - Las aerolíneas más económicas, como SpiceJet, GO FIRST, e Indigo, parecen tener precios similares, sugiriendo competencia directa entre ellas

* Mercado:
    - Vistara y Air India probablemente ofrecen servicios de mayor calidad o dirigidos a clientes premium, lo que justifica sus precios más elevados.
    - AirAsia, Indigo, SpiceJet, y GO FIRST parecen competir en el segmento de aerolíneas económicas.

"""

"""
DEPRECATED: VALOR SESGADO POR DIFERENCIA DE PRECIOS EN CLASES
def graph_gen(data, colors, size=(), img=False):
    data_graph = data.groupby('airline')['price'].mean().reset_index()
    data_graph = data_graph.sort_values(by='price', ascending=False)

    info_graph = {
        'title' : 'Precio medio del boleto por aerolínea',
        'x_name' : 'Aerolínea',
        'y_name' : 'Precio (INR)',
        'x_data' : 'airline',
        'y_data' : 'price'
    }
    
    gen_bar(data_graph, colors, info_graph, size, img)
"""
def graph_gen(data, colors, size=(), img=False):
    
    #Genera una gráfica de barras que muestra el precio promedio del boleto por aerolínea,
    #separado por clase (Economy y Business), y ordenado de mayor a menor por precio promedio total.
    
    # Calcular el precio promedio total por aerolínea (sin importar clase) para ordenar
    order = data.groupby('airline')['price'].mean().sort_values(ascending=False).index
    
    # Agrupar por aerolínea y clase, calcular precio promedio
    data_graph = data.groupby(['airline', 'class'])['price'].mean().reset_index()
    
    data_graph['airline'] = pd.Categorical(data_graph['airline'], categories=order, ordered=True)
    data_graph = data_graph.sort_values(by='airline')
    
    info_graph = {
        'title': 'Precio Medio del Boleto por Aerolínea y Clase',
        'x_name': 'Aerolínea',
        'y_name': 'Precio Promedio (INR)',
        'x_col': 'airline',
        'y_col': 'price',
        'hue_col': 'class',
        'legend': 'Clase'
    }

    gen_bar_3C(data_graph, colors, info_graph, size, img)

