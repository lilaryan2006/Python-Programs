import pandas as pd
import numpy as np
data={'Name':['Motu','Patlu','Nobita','Gian','Shinchan'],
      'Qualification':['Fighter','Fighgter','Lazzier','Bully','Comedian'],
      'Age':['33','33','10','10','5']}
df=pd.DataFrame(data)
print(df)
df.to_csv ("Just.csv")
