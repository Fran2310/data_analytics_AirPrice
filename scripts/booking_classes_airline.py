from .bar_graph_3C import gen_bar_3C

"""
*Distribucion:
    - Vistara y Air India son la aerolíneas que tienen un mayor dominio del mercado, mostrando mayor cantidad de reservas a pesar de sus precios mas elevados, ademas que son las únicas aerolíneas con reservas para clase Business.
    - SpiceJet tiene la menor cantidad de demanda en general de todas las demas
"""
def graph_gen(data, colors, size=(), img=False):
    
    #Genera un gráfico de barras agrupadas para comparar el número de reservas 
    #entre clases Business y Economy por aerolínea
    
    # DataFrame con número de reservas por aerolínea y clase
    class_counts = data.groupby(['airline', 'class']).size().reset_index(name='count')
    
    info_graph = {
        'title': 'Comparativa de Reservas por Clase y Aerolínea',
        'x_name': 'Aerolínea',
        'y_name': 'N° de reservas',
        'legend': 'Clase',
        'x_col': 'airline',
        'y_col': 'count',
        'hue_col': 'class'
    }

    gen_bar_3C(class_counts, colors, info_graph, size, img)





