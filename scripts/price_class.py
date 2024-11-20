import matplotlib.pyplot as plt
import seaborn as sns


"""
*Distribucion:
    - Clase Business: El precio medio del boleto es de aproximadamente 52.000 INR
    - Clase Economy: El precio medio del boleto es de aproximadamente 6.000 INR
    - Los boletos en clase Business son significativamente más caros de media que los billetes en clase Economy
"""

def graph_gen(data, colors, size=(), img=False):
    # Calcular precios medio por clase
    avg_price_class = data.groupby('class')['price'].mean()
    #print("Precio medio del boleto por clase:\n", avg_price_class)

    info_graph = {
        'title': 'Distribución de Precios de Boletos por Clase',
        'x_name': 'Clase de Boletos',
        'y_name': 'Precio del Boleto (INR)',
        'x_data': 'class',
        'y_data': 'price'
    }
    
    boxplot_graph(data, colors, info_graph, size, img)

def boxplot_graph(data_graph, colors, info_graph, size, img):
    if size:
        plt.figure(figsize=size)

    sns.boxplot(
        hue=info_graph['x_data'],
        y=info_graph['y_data'],
        data=data_graph,
        palette=colors[:2], # Usar solo los primeros 2 colores de la paleta
        legend=False 
    )

    plt.title(info_graph['title'], fontsize=12, fontweight='bold', color='#353535')
    plt.xlabel(info_graph['x_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.ylabel(info_graph['y_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.xticks(fontsize=10, color='#353535')
    plt.yticks(fontsize=10, color='#353535')
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()