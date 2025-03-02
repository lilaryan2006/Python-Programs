import pandas as pd
import numpy as np
data=np.array(["Hello","Python","Pandas","Series","My","Name","Is","Aryan"])
s=pd.Series(data,index=["1","2","3","4","5","6","7","8"])
print(s.head(4))
