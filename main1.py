import pandas as pd
D={"Arun":65,"Bala":91,"Charan":74,"Dinesh":80,"Usha":85}
S=pd.Series(D)
print(S[S>75])
