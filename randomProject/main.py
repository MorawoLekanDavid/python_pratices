import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import os
filename = 'randomProject/Sales_Data'
files = [file for file in os.listdir(filename)]
all_months_data = pd.DataFrame()
for file in files:
    df = pd.read_csv(filename+'/'+file)
    all_months_data = pd.concat([all_months_data, df])
    all_sales_data = all_months_data.to_csv('randomProject/all_sales_data.csv',index=False)
all_data = pd.read_csv('randomProject/all_sales_data.csv')
#validation = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')
all_data['Month'] = all_data['Order Date'].str[:2]
all_data = all_data[all_data['Month'] != 'Or']
all_data['Month'] = all_data['Month'].astype('int32')
all_data['Sales'] = pd.to_numeric(all_data['Quantity Ordered']) * pd.to_numeric(all_data['Price Each'])
sales_per_month = all_data['Sales'].groupby(all_data['Month']).sum()
qty_per_month = pd.to_numeric(all_data['Quantity Ordered']).groupby(all_data['Month']).sum()
def get_city(x):
    return x.split(',')[1]
def get_state(x):
    return x.split(',')[2].split(' ')[1]
def get_time(x):
    return x.split(' ')[1]
all_data['City'] = all_data['Purchase Address'].apply(lambda x:x.split(',')[1]+' ('+x.split(',')[2].split(' ')[1]+')')
city_per_month = all_data['Sales'].groupby(all_data['City']).sum()
all_data['Order Time'] = all_data['Order Date'].apply(lambda x: get_time(x))
all_data['Order Time'] = pd.to_datetime(all_data['Order Time'],format='%H:%M').dt.hour
qty_per_hour = pd.to_numeric(all_data['Quantity Ordered']).groupby(all_data['Order Time']).sum()
#qty = [hour for hour,df in qty_per_hour]
print(qty_per_hour)