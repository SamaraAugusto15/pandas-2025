#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df

#%%
df.shape

#%%
df.info(memory_usage='deep')

#%%
df.dtypes

#%%
renamed_columns = {
    "qtdePontos":"qtPontos",
    "descSistemaOrigem": "SistemaOrigem"
}
#%%
df = df.rename(columns=renamed_columns)

#%%
## OU
df = df.rename(columns={"qtdePontos":"qtPontos",
                        "descSistemaOrigem": "SistemaOrigem"})

#%%
df.rename(columns=renamed_columns, inplace=True)

#%%
colunas = ["idCliente", "qtPontos"]
df[colunas]

#%%
#SELECT * FROM df
df

#%%
#SELECT idCliente FROM df
df[["idCliente"]]

#%%
#SELECT idCliente, qtPontos FROM df LIMIT 5
df[["idCliente", "qtPontos"]].head(5)

#%%
#reordenar colunas
#SELECT idCliente, idTransacao, qtPontos FROM df LIMIT 5

df[["idCliente", "idTransacao" ,"qtPontos"]].head(5)

#%%
#ordenar em ordem alfabetica
colunas_2 = df.columns.tolist()

#%%
## OU
colunas_2 = list(df.columns)
#%%
colunas_2.sort()
colunas_2

#%%
df = df[colunas_2]
df