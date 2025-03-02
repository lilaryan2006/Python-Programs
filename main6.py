import pandas as pd
L=[10,45,67,3,43]
S=pd.Series(L,index=['a','b','c','d','e'])
print("The index of the Series is:",S.index)
print("The index of the Series is:",S.dtype)
print("The index of the Series is:",S.size)
print("The index of the Series is:",S.shape)
print("The index of the Series is:",S.hasnans)
            
