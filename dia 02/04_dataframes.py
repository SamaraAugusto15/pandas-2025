#%%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes


#%%
## Amostras
#exibindo as primeiras linhas
df_clientes.head(n=10)

#%%
# exibindo as ultimas linhas
df_clientes.tail(n=10)

#%%
# exibindo de forma sortida
df_clientes.sample(10)

#%%
#um "atributo"
#infos 1° linha 2° colunas
df_clientes.shape

#%%
#nomes das colunas
df_clientes.columns

#%%
df_clientes.index

#%%
df_clientes.info(memory_usage='deep')

#%%
#serie q mostra valores de cada coluna
df_clientes.dtypes
