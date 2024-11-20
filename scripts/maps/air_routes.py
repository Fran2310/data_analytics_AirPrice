import airports_india 
import pandas as pd

import folium

# Limpiando el data set
clean_data_set =  pd.read_csv('./data/Clean_Dataset.csv')
#juntado las columnas para rutas
data_set_reduce = clean_data_set.loc[:,['source_city','destination_city']]
#creando la columan routas sumando los valores de las dos anteriores
data_set_reduce['routes'] = data_set_reduce['source_city'] + ' ' + data_set_reduce['destination_city']

#contamos cuántos vuelos hay para cada ruta
data_set_routes = data_set_reduce['routes'].value_counts()

#falta crear el unique()

print(data_set_routes)


def invertir_ruta(indice):
    palabras = indice.split()
    return ''.join(palabras[::-1])


# Recorrer la serie y comparar índices
for i, (indice, valor) in enumerate(data_set_routes.items()):
    # Asegurarse de no ir fuera del rango
    if i < len(data_set_routes) - 1:
        siguiente_indice = list(data_set_routes.index)[i + 1]
        if invertir_ruta(indice) == siguiente_indice: # Comparar el índice del siguiente elemento con el índice invertido del actual
            

