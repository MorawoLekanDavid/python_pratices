import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Create Frequency table
ages = np.array([20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32])
bins = np.array([18, 25, 35, 60, 100])
group_names = np.array(["Youth", "YoungAdult", "MiddleAged", "Senior"])
age_categories = pd.cut(ages,bins,labels=group_names)
freq_table = pd.DataFrame(age_categories.value_counts())

data = np.random.uniform(size=20)
cdata = pd.cut(data, 4, precision=2)
print(data)
print(cdata)