import matplotlib.pyplot as plt

def gen_hist(data, colors, info_graph, size, img):

    if size:
        plt.figure(figsize=size)

    # Obtener los grupos únicos y asignar colores
    unique_groups = data[info_graph['group_by']].unique()
    color_map = {group: colors[idx] for group, idx in zip(unique_groups, [0, 6])}

    # Iterar sobre cada grupo para graficar
    for group, group_data in data.groupby(info_graph['group_by']):
        plt.hist(group_data[info_graph['x_col']], 
                 bins=30, 
                 alpha=0.5, 
                 label=f"{group} {info_graph.get('label_suffix', '')}", 
                 color=color_map[group])

    # Configuración del gráfico
    plt.title(info_graph['title'], fontsize=12, fontweight='bold', color='#353535')
    plt.xlabel(info_graph['x_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.ylabel(info_graph['y_name'], fontsize=10, fontweight='bold', color='#353535')
    plt.xticks(fontsize=10, color='#353535')
    plt.yticks(fontsize=10, color='#353535')
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.legend()  # Solo se crea una leyenda
    plt.tight_layout()

    # Guardar o mostrar el gráfico
    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()