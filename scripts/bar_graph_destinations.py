import matplotlib.pyplot as plt
import seaborn as sns


def gen_bar_destinations(data_graph, colors, info_graph, size, img):
    
    # Ordenar las categorías del hue de forma consistente en todo el gráfico
    data_graph = data_graph.copy()
    hue_order = (
        data_graph.groupby(info_graph['hue_col'])[info_graph['y_col']]
        .mean()
        .sort_values(ascending=False)
        .index
    )  # Orden global por el promedio de 'y_col'

    if size:
        plt.figure(figsize=size)

    sns.barplot(
        x=info_graph['x_col'], 
        y=info_graph['y_col'], 
        hue=info_graph['hue_col'], 
        data=data_graph, 
        palette=colors,
        hue_order=hue_order
    )
    
    plt.title(info_graph['title'], fontsize=12, fontweight='bold', color='#353535')
    plt.xlabel(info_graph['x_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.ylabel(info_graph['y_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.xticks(rotation=45, fontsize=10, color='#353535')
    plt.yticks(fontsize=10, color='#353535')
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.legend(title=info_graph['legend'], framealpha=0.3)
    plt.tight_layout()
    
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()
