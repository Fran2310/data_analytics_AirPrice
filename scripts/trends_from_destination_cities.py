import matplotlib.pyplot as plt
from palette.generator_palette import extended_palette as palette
import pandas as pd

data = pd.read_csv('./Clean_Dataset.csv')

import matplotlib.pyplot as plt
import pandas as pd

avg_prices_by_destination = data.groupby(['destination_city', 'source_city'])['price'].mean().reset_index()

plt.figure(figsize=(10, 10))

# Obtener las ciudades de destino únicas
destination_cities = avg_prices_by_destination['destination_city'].unique()

# Crear las barras para cada source_city
for i, source_city in enumerate(avg_prices_by_destination['source_city'].unique()):
    # Filtrar por source_city específico
    subset = avg_prices_by_destination[avg_prices_by_destination['source_city'] == source_city]
    
    # Crear las barras para source_city, desplazándolas para que no se sobrepongan
    plt.bar(subset['destination_city'], subset['price'], label=source_city, color=palette[i], width=0.5, align='center')


plt.title('Precio promedio del billete por ciudad de destino')
plt.xlabel('Ciudad de destino')
plt.ylabel('Precio promedio (INR)')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Ciudad de origen')

plt.show()
