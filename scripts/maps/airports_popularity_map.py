import folium

def airports_popularity_map(airports):
    # Crear un mapa centrado en la India
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

    # Iterar sobre el diccionario de diccionarios y agregar los circulos al mapa
    for key, value in airports.items():
        folium.CircleMarker(
            location=value['location'],
            radius=float(value['arrives']/1e7),
            popup=f"A {value['name']} han llegado {value['arrives']} vuelos",
            tooltip= value['name'],
            color = 'black',
            fill_color = 'black'
        ).add_to(m)

    # Guardar el mapa
    m.save('./../web/airports_popularity_map.html')

