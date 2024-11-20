import folium
from airports_india import airports

def airports__popularity_departure_map(airports):
    # Crear un mapa centrado en la India
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    
    #factor de escala de los circulos
    scale = 1000
    
    # Iterar sobre el diccionario de diccionarios y agregar los circulos al mapa
    for key, value in airports.items():
        folium.CircleMarker(
            location=value['location'],
            radius=max(float(value['departures'])/scale, 5),
            popup=f"De {value['name']} han salido {value['departures']} vuelos",
            tooltip= value['city'],
            color = 'green',
            fill_color = 'green'
        ).add_to(m)

    # Guardar el mapa
    m.save('./web/airports_popularity_departure_map.html')


airports__popularity_departure_map(airports)