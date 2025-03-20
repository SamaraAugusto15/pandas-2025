#%%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv")
df

#%%
filtro = (df["idProduto"] == 5) | (df["idProduto"] == 11)
df[filtro]

#%%
filtro_1 = df["idProduto"].isin([5,11])
df[filtro_1]

#%%
clientes= pd.read_csv("../data/clientes.csv")
clientes.head()

filtro_2 = clientes["dtCriacao"].notna()
clientes[filtro_2]

#%%
#mesma coisa
~clientes["dtCriacao"].isna()
clientes["dtCriacao"].notna()
