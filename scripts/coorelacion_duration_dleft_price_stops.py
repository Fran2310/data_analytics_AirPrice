import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df =  pd.read_csv('./data/Clean_Dataset.csv')
#mapeado de la columna stops para pasarlo a datos numericos
stops_mapping = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3
}

df['stops'] = df['stops'].map(stops_mapping)

df_numericas = df[['duration', 'days_left', 'price','stops']]

correlacion = df_numericas.corr()

print(correlacion)

#Grafica de calor
"""plt.figure(figsize=(8, 6))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f', cbar=True) 

# Mostrar el gráfico
plt.title('Matriz de Correlación')
plt.show()"""


#grafica de puntos
plt.figure(figsize=(8, 6))
sns.regplot(x='duration', y='price', data=df, scatter_kws={'s': 10}, line_kws={'color': 'red'})

# Título y etiquetas
plt.title('Relación entre Duración del Vuelo y Precio')
plt.xlabel('Duración del Vuelo (horas)')
plt.ylabel('Precio (en la moneda correspondiente)')

# Mostrar el gráfico
plt.show()


