from .bar_graph import gen_bar


"""
*Mercado: 
    - Tanto Vistara como Air India se muestran como las opciones mas populares a pesar de presentar los precios mas elevados, consolidándose como actores clave en el mercado.
    - Dentro del apartado mas economico, indigo parece tener una ventaja competitiva teniendo una buena popularidad y es una buena opcion dentro del rango de tarifas que maneja en sus boletos, colocandose debajo de SpaceJet y Go First pero encima de AirAsia
    
*Relacion:
    -Posible relacion inversa entre el numero de reservas y el precio (Grafica a desarrollar)
"""

def graph_gen(data, colors, size=(), img=False):
    data_graph = data['airline'].value_counts()

    info_graph = {
        'title' : 'Número de reservas por aerolínea',
        'x_name' : 'Aerolínea',
        'y_name' : 'N° de reservas'
    }
    
    gen_bar(data_graph, colors, info_graph, size, img)