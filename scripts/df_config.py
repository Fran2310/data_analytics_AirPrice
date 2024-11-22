import pandas as pd

data = pd.read_csv('./data/Clean_Dataset.csv')

#mapeo de valores en español
mapping = {
    'zero': 'cero',
    'one': 'uno',
    'two_or_more': 'dos o más'
}

data['stops'] = data['stops'].replace(mapping)

#print(data[['airline', 'stops']])

data.to_csv('./data/Clean_Dataset_config.csv', index=False)
