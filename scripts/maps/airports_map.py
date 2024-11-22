import folium

def airport_map(airports):
    # Crear un mapa centrado en la India
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

    # Iterar sobre el diccionario de diccionarios y agregar marcadores al mapa
    for key, value in airports.items():
        folium.Marker(
            location=value['location'],
            popup=f"<h1>{value['city']}, {value['name']}</h1><img src='{value['img']}' width=300px><p>{value['resume']}</p>",
            tooltip=value['name'],
            icon=folium.Icon(icon='plane', prefix='fa', icon_color='blue')
        ).add_to(m)

    # Mostrar el mapa
    m.save('./../web/airports_map.html')
