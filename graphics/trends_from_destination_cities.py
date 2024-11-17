import matplotlib.pyplot as plt
from palette.generator_palette import extended_palette
import pandas as pd
import seaborn as sns

data = pd.read_csv('./Clean_Dataset.csv')

avg_prices_by_destination = data.groupby(['destination_city', 'source_city'])['price'].mean().reset_index()

plt.figure(figsize=(14, 8))
sns.barplot(x='destination_city', y='price', hue='source_city', data=avg_prices_by_destination, palette=extended_palette)
plt.title('Precio medio del billete por ciudad de destino')
plt.xlabel('Ciudad de Destino')
plt.ylabel('Precio Promedio (INR)')
plt.xticks(rotation=45, ha='right')
plt.grid(True, color=extended_palette[7], linestyle='--', linewidth=0.5)
plt.legend(title='Ciudad de origen')
plt.tight_layout()
plt.show()