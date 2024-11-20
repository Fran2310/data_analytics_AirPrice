from .bar_graph_3C import gen_bar_3C

"""
*Distribucion:
    - Vistara y Air India tienen los precios promedio de boletos más altos y son las únicas aerolíneas con reservas para Business Class
    - SpiceJet tiene la menor cantidad de reservas en general.
"""
def graph_gen(data, colors, size=(), img=False):
    
    #Genera un gráfico de barras agrupadas para comparar el número de reservas 
    #entre clases Business y Economy por aerolínea
    
    # DataFrame con número de reservas por aerolínea y clase
    class_counts = data.groupby(['airline', 'class']).size().reset_index(name='count')
    
    info_graph = {
        'title': 'Comparación de Reservas por Clase (Business vs Economy) por Aerolínea',
        'x_name': 'Aerolínea',
        'y_name': 'Número de Reservas',
        'legend': 'Clase',
        'x_col': 'airline',
        'y_col': 'count',
        'hue_col': 'class'
    }
    
    gen_bar_3C(class_counts, colors, info_graph, size, img)





