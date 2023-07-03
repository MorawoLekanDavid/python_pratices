import numpy as np
import pandas as pd
from pandas import DataFrame,Series
filename = 'accenture/dataset/ReactionTypes.csv'
df = pd.read_csv(filename)
#validate = df[df.isna().any(axis=1)]
df = df.dropna()
df['Type'] = df['Type'].astype('string')
df['Sentiment'] = df['Sentiment'].astype('string')
df = df.rename(columns={'Type':'Reaction Type'})

# The clean dataset
df = df.to_csv('accenture/dataset/clean_dataset/ReactionType.csv',index=False)
df = pd.read_csv('accenture/dataset/clean_dataset/ReactionType.csv')
validate = df[df.isna().any(axis=1)]
print(validate)