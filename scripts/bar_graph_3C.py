import matplotlib.pyplot as plt
import seaborn as sns


def gen_bar_3C(data_graph, colors, info_graph, size, img):
    
    #Genera un gráfico de barras utilizando seaborn, configurable
    
    if size:
        plt.figure(figsize=size)
    
    sns.barplot(
        x=info_graph['x_col'], 
        y=info_graph['y_col'], 
        hue=info_graph['hue_col'], 
        data=data_graph, 
        palette=colors
    )
    
    plt.title(info_graph['title'], fontsize=12, fontweight='bold', color='#353535')
    plt.xlabel(info_graph['x_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.ylabel(info_graph['y_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.xticks(rotation=45, fontsize=10, color='#353535')
    plt.yticks(fontsize=10, color='#353535')
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.legend(title=info_graph['legend'])
    plt.tight_layout()
    
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()