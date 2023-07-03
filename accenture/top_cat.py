import numpy as np
import pandas as pd
import os
df = pd.read_csv('accenture/dataset/clean_dataset/content_cat.csv')
cat_sum = df['Score'].groupby(df['Category']).sum().reset_index()
larg = cat_sum.nlargest(5,'Score')
pivot_table = pd.pivot_table(df,values='Score',columns='Category',aggfunc=np.sum)
category_names = pivot_table.columns
category_sums = pivot_table.loc[:, category_names]
category_sum_values = category_sums.values.flatten()
values = [value for value in category_sum_values]
#merged_df = pd.concat([df,pivot_table], axis=0, join='outer', ignore_index=False)
#merged_df = df.join(pivot_table, on=None, how='left')
for val in values:
    df['Cat_score'] = val
    print(df)
