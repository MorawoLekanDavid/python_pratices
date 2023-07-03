import numpy as np
import pandas as pd
df = pd.read_csv('accenture/dataset/clean_dataset/content_cat.csv')
cat_sum = df['Score'].groupby(df['Category']).sum().reset_index()
larg = cat_sum.nlargest(5, 'Score')
pivot_table = pd.pivot_table(cat_sum,values='Score', columns='Category')
#merged_df = pd.concat([df,pivot_table],axis=0)
#merged_df = pd.concat([df,larg],axis=1)
pivot_table.to_csv('accenture/dataset/clean_dataset/cat_score.csv',index=False)
larg.to_csv('accenture/dataset/clean_dataset/top_cat.csv',index=False)
#df_read = pd.read_csv('accenture/dataset/clean_dataset/large_cat.csv')
print(larg)
