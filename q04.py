##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 


import pandas as pd

df = pd.read_csv("tbl1.tsv", sep="\t")
print(sorted([string.upper() for string in set(df["_c4"])]))