import pandas as pd
data = pd.read_csv('export.csv')

country_data = {}
for index, row in data.iterrows():
    country = row['country']
    if country not in country_data:
        country_data[country] = []
    country_data[country].append(row)

for country, data in country_data.items():
    df = pd.DataFrame(data)
    df.to_csv(f'{country}.csv', index=False)