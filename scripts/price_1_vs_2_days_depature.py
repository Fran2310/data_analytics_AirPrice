import matplotlib.pyplot as plt


def graph_gen(data, colors, size=(), img=False):
    data_filtered = data[data['days_left'].isin([1, 2])]

    info_graph = {
        'title': 'Distribución de precios de billetes de 1 y 2 días antes de la salida',
        'x_name': 'Precio (INR)',
        'y_name': 'N° Tickets (frecuencia)'
    }
    
    gen_hist(data_filtered, colors, info_graph, size, img)

def gen_hist(data, colors, info_graph, size, img):
    if size:
        plt.figure(figsize=size)

    color_map = {1: colors[0], 2: colors[6]}

    for days, group_data in data.groupby('days_left'):
        plt.hist(group_data['price'], bins=30, alpha=0.5, label=f'{days} Días Antes', color=color_map[days])

    plt.title(info_graph['title'])
    plt.xlabel(info_graph['x_name'])
    plt.ylabel(info_graph['y_name'])
    plt.grid(True, color=colors[7], linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()

    if img:
        plt.savefig(f"./visualizations/graph_img/{info_graph['title']}.png")
    else:
        plt.show()
