import pandas as pd
from scripts import price_days_left, trends_from_destination_cities, airline_popularity, avg_price_airline, price_1_vs_2_days_depature


data = pd.read_csv('./data/Clean_Dataset.csv')

palette_colors = ['#00a5c4', '#00596a', '#d5f4f4', '#738484', '#a172a5', '#573e59', '#63529b', '#352c53']

avg_price_airline.graph_gen(data, palette_colors, (8,6), True)

airline_popularity.graph_gen(data, palette_colors, (8,6), True)

price_1_vs_2_days_depature.graph_gen(data, palette_colors, (8,6), True)

price_days_left.graph_gen(data, palette_colors, (11,6), True)

trends_from_destination_cities.graph_gen(data, palette_colors, (11,6), True)







