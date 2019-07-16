##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 

import pandas as pd

df = pd.read_csv("tbl0.tsv", sep="\t")
print(df.groupby(["_c1"])["_c1"].count())