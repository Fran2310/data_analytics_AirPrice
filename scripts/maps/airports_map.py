import folium 
from airports import Delhi

loca=Delhi['location']
ciudad = Delhi['ciudad']
img = Delhi['img']
resume = Delhi['resume']
name = Delhi['name']

m = folium.Map(location=loca, zoom_start=25)

folium.Marker(loca, 
              popup=f"<h1> Aereopuerto internacional {name}</h1><h2>Ciudad: {ciudad}</h2><img src={img} width=400px><p> {resume} </p>",
              tooltip=f"{name}, {ciudad}",
              icon = folium.Icon(icon='plane', icon_color='white', color='blue')).add_to(m)

m.save('map.html')