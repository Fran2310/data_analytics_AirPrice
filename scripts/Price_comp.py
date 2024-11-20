import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

"""
-Se observa una gran brecha de precio tomando como referencia Vistara, siendo esta que tiene el boleto para la clase Economy mas cara de las aerolineas estudiadas.
AirAsia siendo la mas barata de estas representa una diferencia de casi 3715 unidades monetarias con respecto a Vistara, las demas tienen la brecha de precio menor.

-Se observa que Go Firts, Indigo y AirAsia tienen los precios mas competivivos del mercado manteniendo un equilibrio en la accesibilidad de sus boletos para la clase economica
con respecto a Vistara, AirIndia y SpiceJet que mantienen precios mas elevados en sus boletos

"""
def graph_gen(data, colors, size=(), img=False):

    precio_promedio = data.groupby(['class', 'airline'])['price'].mean().reset_index()

    precio_promedio['price_diff'] = precio_promedio.groupby('class')['price'].transform(lambda x: x.max() - x)

    precio_promedio = precio_promedio.sort_values(by=['class', 'price_diff'])

    info_graph = {
        'title': 'Precios y Diferencia de Precios entre Aerolíneas por Clase',
        'x_name': 'Aerolinea',
        'y_name': 'Precio y Diferencia de Precio',
        'x_data': precio_promedio['airline'],
        'y_data': precio_promedio['price'],
        'price_diff_data': precio_promedio['price_diff'],
        'class_data': precio_promedio['class'],
        'xticks_step': 2  
    }

    gen_bar(info_graph, colors, size, img)


def gen_bar(info_graph, colors, size, img):
    if size:
        plt.figure(figsize=size)

    x_data = info_graph['x_data']
    y_data = info_graph['y_data']
    price_diff_data = info_graph['price_diff_data']
    class_data = info_graph['class_data']

    fig, ax = plt.subplots()

    sns.barplot(x=x_data, y=y_data, hue=class_data, palette=colors, ax=ax, dodge=True, ci=None)

    ax2 = ax.twinx() 
    ax2.bar(x_data, price_diff_data, width=0.4, alpha=0.3, color='gray', label='Diferencia de precio')
    ax2.set_ylabel('Diferencia de Precio', color='gray')

    ax.set_title(info_graph['title'])
    ax.set_xlabel(info_graph['x_name'])
    ax.set_ylabel(info_graph['y_name'])
    ax.legend(title='Clase', loc='upper left')
    ax2.legend(title='Diferencia de Precio', loc='upper right')

    # Mejorar visualización
    plt.xticks(rotation=45)
    plt.tight_layout()

    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png", bbox_inches='tight')
    else:
        plt.show()