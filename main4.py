import pandas as pd
import numpy as np
Section=['A','B','C']
Contribution=np.array([6700,5500,np.NaN])
S=pd.Series(data=Contribution,index=Section)
print(S)
