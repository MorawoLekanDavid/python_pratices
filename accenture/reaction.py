import numpy as np
import pandas as pd
import uuid
from pandas import DataFrame,Series
filename = 'accenture/dataset/Reactions.csv'
df = pd.read_csv(filename)
#validate = df[df.isna().any(axis=1)]
df = df.dropna()
df['Datetime'] = df['Datetime'].astype('datetime64[ns]')
df['Type'] = df['Type'].astype('string')
df['Content ID'] = df['Content ID'].astype('string').apply(lambda x: uuid.UUID(x))
df['User ID'] = df['User ID'].astype('string').apply(lambda x: uuid.UUID(x))
df = df.drop('User ID',axis=1)
df = df.rename(columns={'Type':'Reaction Type'})
# The clean dataset
df = df.to_csv('accenture/dataset/clean_dataset/Reaction.csv',index=False)
df = pd.read_csv('accenture/dataset/clean_dataset/Reaction.csv')
print(df)