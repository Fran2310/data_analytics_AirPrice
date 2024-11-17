import matplotlib.pyplot as plt
import pandas as pd


def gen_bar(data_graph, colors, info_graph, size=(), img=False):
    """
    Genera un gráfico de barras para un DataFrame o Serie.

    data_graph: Puede ser un DataFrame o una Serie.
    colors: Lista de colores para las barras.
    info_graph: Diccionario con información del gráfico (títulos y nombres de ejes).
    size: Tupla opcional para definir el tamaño del gráfico.
    img: Booleano, True para guardar el gráfico como imagen.
    """
    
    if size:
        plt.figure(figsize=size)

    if isinstance(data_graph, pd.Series):

        x_data, y_data = data_graph.index, data_graph.values
    elif isinstance(data_graph, pd.DataFrame):

        x_data = data_graph[info_graph['x_data']]
        y_data = data_graph[info_graph['y_data']]
    else:
        raise ValueError("El parámetro 'data_graph' debe ser un DataFrame o una Serie.")

    plt.bar(x_data, y_data, color=colors)

    plt.title(info_graph['title'])
    plt.xlabel(info_graph['x_name'])
    plt.ylabel(info_graph['y_name'])
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.xticks(rotation=45)

    if img:
        plt.savefig(f"./graph_img/{info_graph['title']}.png")
    else:
        plt.show()