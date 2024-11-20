import folium

def airports_popularity_arrives_map(airports):
    # Crear un mapa centrado en la India
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    
    #factor de escala de los circulos
    scale = 1000
    
    # Iterar sobre el diccionario de diccionarios y agregar los circulos al mapa
    for key, value in airports.items():
        folium.CircleMarker(
            location=value['location'],
            radius=max(float(value['arrives'])/scale, 5),
            popup=f"A {value['name']} han llegado {value['arrives']} vuelos",
            tooltip= value['city'],
            color = 'red',
            fill_color = 'red'
        ).add_to(m)

    # Guardar el mapa
    m.save('./web/airports_popularity_arrives_map.html')
