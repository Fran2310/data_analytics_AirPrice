from .bar_graph import gen_bar


def graph_gen(data, colors, size=(), img=False):
    data_graph = data.groupby('airline')['price'].mean().reset_index()
    data_graph = data_graph.sort_values(by='price', ascending=False)

    info_graph = {
        'title' : 'Precio promedio general de boleto por aerolinea',
        'x_name' : 'Aerolineas',
        'y_name' : 'Precios (INR)',
        'x_data' : 'airline',
        'y_data' : 'price'
    }
    
    gen_bar(data_graph, colors, info_graph, size, img)