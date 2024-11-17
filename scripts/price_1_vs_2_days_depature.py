import matplotlib.pyplot as plt
from palette.generator_palette import extended_palette as palette
import pandas as pd

data_main = pd.read_csv('./Clean_Dataset.csv')

one_day_before = data_main[data_main['days_left'] == 1]
two_days_before = data_main[data_main['days_left'] == 2]

plt.hist(one_day_before['price'], bins=30, alpha=0.5, label='1 Dia Antes', color=palette[0])

plt.hist(two_days_before['price'], bins=30, alpha=0.5, label='2 Dias Antes', color=palette[3])

plt.title('Distribución de precios de billetes de 1 y 2 días antes de la salida')
plt.xlabel('Precio')
plt.ylabel('N° Tickets (frecuencia)')
plt.grid(True, color=palette[7], linestyle='--', linewidth=0.5)
plt.legend()
plt.show()