import pandas as pd

from scripts import price_days_left, trends_from_destination_cities, airline_popularity, avg_price_airline, price_1_vs_2_days_depature, price_class, dist_price_class, booking_classes_airline, stops_duration_price, Price_comp

data = pd.read_csv('./data/Clean_Dataset_config.csv')

palette_colors = ['#00a5c4', '#00596a', '#d5f4f4', '#738484', '#a172a5', '#573e59', '#63529b', '#352c53']


airline_popularity.graph_gen(data, palette_colors, (8,6), True)

booking_classes_airline.graph_gen(data, [palette_colors[1], palette_colors[0]], (8, 6), True)

avg_price_airline.graph_gen(data, palette_colors[:2], (8,6), True)

price_1_vs_2_days_depature.graph_gen(data, palette_colors, (8,6), True)

trends_from_destination_cities.graph_gen_economy(data, palette_colors, (11,6), True)

trends_from_destination_cities.graph_gen_business(data, palette_colors, (11,6), True)

price_days_left.graph_gen(data, palette_colors, (11,6), True)

price_days_left.graph_gen_3line(data, palette_colors, (11,6), True)

stops_duration_price.graph_gen_stops(data, palette_colors, (8, 6), True)

stops_duration_price.graph_gen_duration(data, palette_colors, (8, 6), True)

price_class.graph_gen(data, palette_colors, (8,6), True)

dist_price_class.graph_gen(data, palette_colors, (8,6), True)

#booking_classes_airline.graph_gen(data, palette_colors, (8, 6), True)

#stops_duration_price.graph_gen_stops(data, palette_colors, (8, 6), True)

#stops_duration_price.graph_gen_duration(data, palette_colors, (8, 6), True)

#airports_popularity_arrives_map.airports_popularity_arrives_map(airp) #map airports popularity arrives html
#airports_popularity_departure_map.airports__popularity_departure_map(airp) #map airports popularity departure html





