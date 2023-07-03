import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.standard_normal(size=(6,4)),index=['one','two','three','four','five','six'],
                   columns=pd.Index(['A','B','C','D'],name='Genus'))
print(df.plot.bar())