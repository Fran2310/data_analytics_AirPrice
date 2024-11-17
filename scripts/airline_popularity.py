import matplotlib.pyplot as plt
from .bar_graph import gen_bar

data_main = pd.read_csv('./Clean_Dataset.csv')

airline_popularity = data_main['airline'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(airline_popularity.index, airline_popularity.values, color=palette)

plt.title('Número de reservas por vuelo')
plt.xlabel('Aerolineas')
plt.ylabel('N° de reservas')
plt.grid(True, color=palette[7], linestyle='--', linewidth=0.5)
plt.xticks(rotation=45)

plt.show() 
