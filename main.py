import pandas as pd
from scripts import trends_from_destination_cities, airline_popularity, avg_price_airline


data = pd.read_csv('./data/Clean_Dataset.csv')

palette_colors = ['#00a5c4', '#00596a', '#d5f4f4', '#738484', '#a172a5', '#573e59', '#63529b', '#352c53']

trends_from_destination_cities.graph_gen(data, palette_colors, (10,6))

airline_popularity.graph_gen(data, palette_colors, (8,6))

avg_price_airline.graph_gen(data, palette_colors, (6, 6))