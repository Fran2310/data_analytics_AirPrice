import folium

import folium
import numpy as np
import pandas as pd
import json
from airports_india import airports

with open('./scripts/maps/India_States_2020_compressed_topo.json') as f:
  states_topo = json.load(f)
  
#buscando la información en nuestro clear
data_main = pd.read_csv('./data/Clean_Dataset.csv', encoding='utf-8')
data_arrives = data_main['source_city'].value_counts()

#convirtiendo en data frame
data_arrives_df = data_arrives.reset_index()
data_arrives_df.columns = ['Province', 'Count']

#creamos un diccionario para poder cambiar los nombres de las ciudades 
#de nuestro df y que coincidan con el nombre de los estados del json
nuevos_valores = {
    'Mumbai': 'MAHARASHTRA',
    'Delhi':'DELHI',
    'Bangalore':'KARNATAKA',
    'Kolkata' :'WEST BENGAL',
    'Hyderabad' : 'TELANGANA',
    'Chennai':'TAMIL NADU'
}

#Remplazando valores
data_arrives_df['Province'] = data_arrives_df['Province'].replace(nuevos_valores)

#creamos el mapa
folium_map = folium.Map(location=[19, 80],
                        zoom_start=4,
                        tiles="OpenStreetMap")
folium.Choropleth(geo_data=states_topo,
             topojson='objects.India_States_2020_compressed',
             key_on='feature.properties.state_name',
             data=data_arrives_df, 
             columns=['Province','Count'], 
             fill_color='GnBu', 
             fill_opacity=0.7, 
             line_opacity=0.5).add_to(folium_map)

# Añadir popups
for key, value in airports.items():
    popup_content = f"<h2>{value['city']}, {value['name']}</h2><h5>Desde este aeropuerto en {value['city']} han salido {value['departures']} personas.</h5>"
    popup = folium.Popup(popup_content, max_width=200) 
    folium.Marker(
        location=value['location'],
        popup=popup,
        tooltip=value['name'],
        icon=folium.Icon(icon='plane', prefix='fa', icon_color='white', color='green')
    ).add_to(folium_map)

# Guardar el mapa en un archivo HTML
folium_map.save('./web/airports_popularity_departure_map.html')
