##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

import pandas as pd

df = pd.read_csv("tbl0.tsv", sep="\t")

table = pd.DataFrame({
    "_c0": [],
    "lista": []
})

for letter in sorted(df["_c1"].unique()):
    lista = ":".join(map(str, sorted(df[df["_c1"]==letter]["_c2"])))
    table = table.append(
        {"_c0": letter, "lista": lista}, ignore_index=True
    )

print(table)