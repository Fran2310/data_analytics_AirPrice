from .bar_graph import gen_bar


def graph_gen(data, colors, size=(), img=False):
    data_graph = data['airline'].value_counts()

    info_graph = {
        'title' : 'Número de reservas por aerolinea',
        'x_name' : 'Aerolineas',
        'y_name' : 'N° de reservas'
    }
    
    gen_bar(data_graph, colors, info_graph, size, img)