import matplotlib.pyplot as plt
from palette.generator_palette import extended_palette as palette
import pandas as pd
from bar_graph import gen_bar

data_main = pd.read_csv('./data/Clean_Dataset.csv')

avg_price_airline = data_main.groupby('airline')['price'].mean().reset_index()
avg_price_airline = avg_price_airline.sort_values(by='price', ascending=False)

category_x = avg_price_airline['airline']
price_y = avg_price_airline['price']

plt.figure(figsize=(8, 6))
plt.bar(category_x, price_y, color=palette)

plt.title('Precio promedio general de boleto por aerolinea')
plt.xlabel('Aerolineas')
plt.ylabel('Precios (INR)')
plt.grid(True, color=palette[7], linestyle='--', linewidth=0.5)
plt.xticks(rotation=45)

plt.show()
