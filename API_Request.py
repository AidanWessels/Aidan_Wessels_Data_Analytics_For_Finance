import numpy as np
import numpy_financial as npf
import pandas as pd

data = pd.read_csv('all_currencies.csv')

unique_symbols = data['Symbol'].unique()

np.sort(data.Symbol.unique())

rate1 = 0.5

print(npf.npv(rate1, data['High']))




