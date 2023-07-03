import numpy as np
import pandas as pd
import os
filename = 'accenture/dataset/clean_dataset'
files = [file for file in os.listdir(filename)]
all_data = pd.DataFrame()
df0 = pd.read_csv(os.path.join(filename, files[0]))
df1 = pd.read_csv(os.path.join(filename, files[1]))
df2 = pd.read_csv(os.path.join(filename, files[2]))
df_merge = df1.merge(df0, on='Content ID')
df_merge = df_merge.merge(df2, on='Reaction Type')
df_column = ['Content ID', 'Content Type', 'Category', 'Reaction Type','Score','Sentiment','Datetime']
df = df_merge[df_column]
df.to_csv('accenture/dataset/clean_dataset/content_cat.csv',index=False)
df_read = pd.read_csv('accenture/dataset/clean_dataset/content_cat.csv')
print(df_read.head())