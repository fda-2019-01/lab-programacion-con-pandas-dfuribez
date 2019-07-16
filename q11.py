##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas as pd 
from operator import itemgetter as ig

df = pd.read_csv("tbl2.tsv", sep="\t")

table = pd.DataFrame({"_c0": [], "lista": []})
table["_c0"] = table["_c0"].astype(int)

for element in sorted(df["_c0"].unique()):
    mask = df["_c0"] == element
    elements = list(zip(df[mask]["_c5a"], df[mask]["_c5b"]))
    lista = [":".join(map(str, pair)) for pair in sorted(elements, key=ig(0))]
    lista = ",".join(lista)

    table = table.append(
        {
            "_c0": element,
            "lista": lista
        },
        ignore_index=True
    )

print(table)
