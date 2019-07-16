##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd 

df = pd.read_csv("tbl1.tsv", sep="\t")

table = pd.DataFrame({"_c0": [], "lista": []})
table["_c0"] = table["_c0"].astype(int)

for element in sorted(df["_c0"].unique()):
    lista = ",".join(sorted(df[df["_c0"]==element]["_c4"]))
    table = table.append(
        {
            "_c0": element,
            "lista": lista,
        },
        ignore_index=True
    )
print(table)