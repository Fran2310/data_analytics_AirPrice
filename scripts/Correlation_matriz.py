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

     'title': 'Matriz correlacion entre cantidad de reservas y el precio ',
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

        x_data = info_graph['x_data']
        y_data = info_graph['y_data']
    
        df = pd.DataFrame({
        info_graph['x_name']: x_data,
        info_graph['y_name']: y_data
    })
    
        correlacion_matrix = df.corr()
    
    # Crear la matriz de calor
        sns.heatmap(correlacion_matrix, annot=True, cmap=colors, cbar=True, linewidths=0.5, annot_kws={"size": 16})
    
    # Títulos y etiquetas
        plt.title(info_graph['title'])
        plt.xlabel(info_graph['x_name'])
        plt.ylabel(info_graph['y_name'])
    
    # Ajustar la visualización
        plt.tight_layout()
    
    # Guardar la imagen si se especifica
        if img:
            plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png", bbox_inches='tight')
        else:
            plt.show()


