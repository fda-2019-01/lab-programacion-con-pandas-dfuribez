##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

import pandas as pd 

df0 = pd.read_csv("tbl0.tsv", sep="\t")
df2 = pd.read_csv("tbl2.tsv", sep="\t")

df = pd.merge(df0, df2, on="_c0")[["_c5a", "_c5b"]]

print(df.groupby("_c5a").sum())