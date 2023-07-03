import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import os
filename = 'randomProject/Sales_Data'
files = [file for file in os.listdir(filename)]
df = pd.DataFrame()
for file in files:
    sales_data = pd.read_csv(filename+'/'+file)
    df = pd.concat([df,sales_data])
    all_months_sales = df.to_csv('randomProject/all_sales_datas.csv',index=False)
all_data = pd.read_csv('randomProject/all_sales_datas.csv')
#validation = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')
all_data['Month'] = all_data['Order Date'].str[:2]
all_data = all_data[all_data['Month'] != 'Or']
all_data['Month'] = all_data['Month'].astype('int32')
all_data['Sales'] = pd.to_numeric(all_data['Quantity Ordered']) * pd.to_numeric(all_data['Price Each'])
sales_per_month = all_data['Sales'].groupby(all_data['Month']).sum()
qty_per_month = pd.to_numeric(all_data['Quantity Ordered']).groupby(all_data['Month']).sum()
print(sales_per_month.max(),qty_per_month.max())