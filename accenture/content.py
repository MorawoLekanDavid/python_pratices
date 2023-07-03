import numpy as np
import pandas as pd
from pandas import DataFrame,Series
filename = 'accenture/dataset/Content.csv'
df = pd.read_csv(filename)
#validate = df[df.isna().any(axis=1)]
df = df.dropna()
df['Type'] = df['Type'].astype('string')
df['Category'] = df['Category'].astype('string')
df['URL'] = df['URL'].astype('string')
df = df.rename(columns={'Type':'Content Type'})
df = df.drop(['URL','User ID'],axis=1)
# The clean dataset
df = df.to_csv('accenture/dataset/clean_dataset/Contents.csv',index=False)
df = pd.read_csv('accenture/dataset/clean_dataset/Contents.csv')
validate = df[df.isna().any(axis=1)]
print(validate)