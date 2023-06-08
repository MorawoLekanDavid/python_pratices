import numpy as np
#pure python method
xarr = [1,2,3,4,5]
yarr = [6,7,8,9,10]
cond = [True,False,False,False,False]
#for i in range(len(cond)):
    #if cond[i] == True:
       # print(xarr[i])
    #else:
        #print(yarr[i])
#numpy method
xar = np.array(xarr)
yar =  np.array(yarr)
conds =  np.array(cond)
result = np.where(conds,xar,yar)
#print(result)

#Replace all the +ve values with 2 and the -ve values with -2
sample = np.random.standard_normal(size=(4,4))
print(sample)
result = np.where(sample>0,2,-2)
print(result)