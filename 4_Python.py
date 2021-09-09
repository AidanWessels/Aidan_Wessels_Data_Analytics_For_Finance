import numpy as np
import numpy_financial as npf
import pandas as pd

data = pd.read_csv('all_currencies.csv')

#4a_Define a custom function to create reuseable code

grouped_data = data[(data.Symbol == '$$$')]

def fill_missiing_data(data, fillvalue=0):
    data = data.copy()
    for i, value in enumerate(data['Market Cap'].values):
        if np.isnan(value):
            data['Market Cap'][i] = fillvalue
    return(data)

print(fill_missiing_data(grouped_data))

#4b Numpy

print(np.sort(data.Symbol.unique()))

#4c Dictionary or Lists


