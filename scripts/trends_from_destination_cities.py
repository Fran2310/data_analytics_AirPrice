import matplotlib.pyplot as plt
import seaborn as sns

def graph_gen(data, colors, size=(), img=False):
    #Tendencias de precios en ciudades de origen y destino
    
    #dataframe precios promedio por destino
    data_graph = data.groupby(['destination_city', 'source_city'])['price'].mean().reset_index()
    
    info_graph = {
                'title': 'Precio medio del Boleto por ciudad de destino',
                'x_name': 'Ciudad de Destino',
                'y_name' : 'Precio Promedio (INR)',
                'legend': 'Ciudad de origen'
    }
    
    bar_graph_seaborn(data_graph, colors, info_graph, size, img)

def bar_graph_seaborn(data_graph, colors, info_graph, size, img):
    if size:
        plt.figure(figsize=size)
    
    sns.barplot(x='destination_city', y='price', hue='source_city', data=data_graph, palette=colors)
    plt.title(info_graph['title'])
    plt.xlabel(info_graph['x_name'])
    plt.ylabel(info_graph['y_name'])
    plt.xticks(rotation=45)
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.legend(title=info_graph['legend'])
    plt.tight_layout()
    
    if img:
        plt.savefig(f"./graph_img/{info_graph['title']}.png")
    else:
        plt.show()