import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt, timedelta

#2b Import a CSV File into a Pandas DataFrame
data = pd.read_csv('all_currencies.csv')
data2 = pd.read_csv('crypto_prices.csv')

#print(data.columns)
#print(data2.columns)


#print(data['Symbol'].nunique())

#3 Analysing Data
#3a.1. Sort
data_date_sort = data.sort_values(by=['Date'], axis=0, na_position='last')
data_high_sort = data.sort_values(by=['High'], axis=0, ascending = 0, na_position='last')

#print(data_date_sort)
#print(data_high_sort[['Date','High','Symbol']])

#3a.2 Index
indexed_data = data.index[data['Symbol'] == 'NANOX']

#print(data[indexed_data])

#3a.3 Group
grouped_data = data[(data.Symbol == 'BSC')]
grouped_data2 = data2[(data2.Symbol == 'BSC')]
data_highest_per_currency = data[data.groupby('Symbol').High.transform('max') == data['High']]

#print(grouped_data2)

#print(data_highest_per_currency[['Date','Symbol','High']])

#3b Replacing missing values

data[['Market Cap']] = data[['Market Cap']].fillna(method="bfill",axis=0).fillna(method="ffill",axis=0)

#print(data)

#3d Looping, iterrows


#for label, row in data.iterrows():
#    data.loc[label,'Circulating Supply'] = row['Market Cap']/row['Close']
#print(data)

#3d Merge DataFrames

data2.rename(columns={"DateTime": "Date"}, inplace=True)

data['Date'] = pd.to_datetime(data['Date'])
data2['Date']=pd.to_datetime(data2['Date'])
data2['Date'] = pd.to_datetime(data2["Date"].dt.strftime('%Y-%m-%d'))


grouped_data = data[(data['Symbol']=='1337') & (data['Date']=='2017-06-26')]

grouped_data2 = data2.loc[(data2['Date'] == '2017-06-26')]
grouped_data2 = grouped_data2[(grouped_data2['Symbol']=='1337')]

#print(grouped_data)
#print(grouped_data2)

ETH_data = data[(data['Symbol']=='ETH')]
ETH_data2 = data2[(data2['Symbol']=='ETH')]


ETH_merged_data = ETH_data.merge(ETH_data2, how='inner', left_on=["Symbol","Date"], right_on=["Symbol","Date"])
print(ETH_merged_data.head())