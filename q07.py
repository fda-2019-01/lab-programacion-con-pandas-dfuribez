##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 

import pandas as pd

df = pd.read_csv("tbl0.tsv", sep="\t")
df["suma"] = df["_c0"] + df["_c2"]
print(df)