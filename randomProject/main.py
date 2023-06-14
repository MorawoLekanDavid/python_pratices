import numpy as np
import pandas as pd
import os
df = pd.read_csv('randomProject/Sales_Data/Sales_April_2019.csv')
fdir = [file for file in os.listdir("randomProject/Sales_Data")]
print(fdir)
