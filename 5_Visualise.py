import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt, timedelta

data = pd.read_csv('all_currencies.csv')
data2 = pd.read_csv('crypto_prices.csv')

#Take a currency - Analyse this over the most recent 5 years in our data

data['Date'] = pd.to_datetime(data['Date'])
dope_data = data[(data.Symbol == 'DOPE')]

start_date = dope_data['Date'].min()
end_date = dope_data['Date'].max()

last_year = end_date - timedelta(year=1)

print(start_date)
print(end_date)
