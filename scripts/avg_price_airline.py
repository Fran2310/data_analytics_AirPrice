from .bar_graph import gen_bar


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