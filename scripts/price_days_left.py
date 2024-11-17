import matplotlib.pyplot as plt
from palette.generator_palette import extended_palette as palette
import pandas as pd

data = pd.read_csv('./data/Clean_Dataset.csv')

max_days_left = data['days_left'].max()


bins = range(0, max_days_left + 3, 3)
labels = [f'{i}-{i+2}' for i in bins[:-1]]  # Etiquetas de los intervalos

# Agrupar los datos por estos intervalos y calcular el precio promedio de cada intervalo
data['days_left_bins'] = pd.cut(data['days_left'], bins=bins, labels=labels, right=False)
avg_prices = data.groupby('days_left_bins')['price'].mean()

plt.figure(figsize=(10, 6))
avg_prices.plot(kind='line', marker='o', color=palette[1])

xticks = range(0, len(avg_prices), 2)  # Definir que se muestren cada 2 días
plt.xticks(xticks, avg_prices.index[xticks], rotation=45)

plt.title('Precio Promedio de Boletos Según Días de Antelación')
plt.xlabel('Días de Antelación (Days Left)')
plt.ylabel('Precio Promedio del Boleto (Price)')
plt.grid(True, color=palette[7], linestyle='--', linewidth=0.5)

plt.show()