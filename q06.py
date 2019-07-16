##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 

import pandas as pd

df = pd.read_csv("tbl0.tsv", sep="\t")
print(df.groupby(["_c1"])["_c2"].sum())