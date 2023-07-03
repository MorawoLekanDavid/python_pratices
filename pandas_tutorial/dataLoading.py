import pandas as pd
from pandas import Series ,DataFrame
filename = 'pandas_tutorial/tutorial2.xlsx'
df = pd.read_excel(filename,sheet_name=None)
print(df)
