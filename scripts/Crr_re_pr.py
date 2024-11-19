import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def graph_gen(data, colors, size=(), img=False):

    cantidad_reservas = data['airline'].value_counts()

    precio_promedio = data.groupby('airline')['price'].mean()

    correlacion_aerolinea = pd.DataFrame({
    'cantidad_reservas': cantidad_reservas,
    'price': precio_promedio
    }).reset_index()

    correlacion_aerolinea = correlacion_aerolinea.sort_values(by='cantidad_reservas')

# Ordenar por la cantidad de reservas para mejorar la visualización
    x_data = correlacion_aerolinea['cantidad_reservas']
    y_data = correlacion_aerolinea['price']

    info_graph = {

     'title': 'Correlacion entre cantidad de reservas y el precio ',
        'x_name': 'Cantidad de reservas',
        'y_name': 'Precio Promedio del Boleto',
        'x_data': x_data,
        'y_data': y_data,
        'xticks_step': 2  #mostrar cada 2 etiquetas en el eje X

    }
    gen_line(info_graph, colors, size, img)


def gen_line(info_graph, colors, size, img):
    if size:
        plt.figure(figsize=size)

    plt.plot(info_graph['x_data'], info_graph['y_data'], marker='o', color=colors[1])

    xticks = range(0, len(info_graph['x_data']), info_graph['xticks_step'])
    plt.xticks(xticks, info_graph['x_data'][xticks], rotation=90)
    plt.title(info_graph['title'])
    plt.xlabel(info_graph['x_name'])
    plt.ylabel(info_graph['y_name'])
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()


