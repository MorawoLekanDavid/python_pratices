import pandas as pd
import numpy as np
from pandas import Series, DataFrame

s1 = pd.Series([7.3, -2.5, 3.4, 1.5],index = ["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index = ["a", "c", "e", "f", "g"])
#print(s1)
#print(s2)
#print(s1 + s2)
#Dataframe Arithmetic
df1 = pd.DataFrame(np.arange(12.).reshape(3,4),columns=list("abcd"))
df2 = pd.DataFrame(np.arange(20.).reshape(4,5),columns=list("abcde"))
ad = df1 + df2
a = pd.isna(ad)
ad[a] = 0.0
print(ad)