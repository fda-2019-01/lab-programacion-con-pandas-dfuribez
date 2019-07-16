##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas as pd

df = pd.read_csv("tbl0.tsv", sep="\t")
df["ano"] = list(map(lambda _: _[0:4], df["_c3"]))
print(df)