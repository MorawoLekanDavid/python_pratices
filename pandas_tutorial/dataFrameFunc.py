import numpy as np 
import pandas as pd
from pandas import Series, DataFrame

df = pd.DataFrame(np.random.standard_normal(size=(4,3)),columns=list("abc"), 
                    index=["Utah", "Ohio","Texas", "Oregon"])

def f1(x):
    return x.max() - x.min()
print(df)
print(df.apply(f1,axis='columns'))