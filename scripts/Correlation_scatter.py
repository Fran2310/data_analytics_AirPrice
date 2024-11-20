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
    gen_scatter(info_graph, colors, size, img)

def gen_scatter(info_graph, colors, size, img):
    # Si se proporciona un tamaño, ajusta la figura
    if size:
        plt.figure(figsize=size)
    
    x_data = info_graph['x_data']
    y_data = info_graph['y_data']
    
    df = pd.DataFrame({
        info_graph['x_name']: x_data,
        info_graph['y_name']: y_data
    })
    
    sns.regplot(x=info_graph['x_name'], y=info_graph['y_name'], data=df, 
                scatter_kws={'color': colors[0], 's': 50}, 
                line_kws={'color': colors[1], 'linewidth': 2}, 
                ci=None,  
                scatter=True)
    
    plt.title(info_graph['title'])
    plt.xlabel(info_graph['x_name'])
    plt.ylabel(info_graph['y_name'])
    
    plt.tight_layout()
    
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png", bbox_inches='tight')
    else:
        plt.show()

