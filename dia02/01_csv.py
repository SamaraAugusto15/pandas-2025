#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

#%%
df.to_csv("clientes.csv", index=False)

#%%
#parquet
df.to_parquet("clientes.parquet", index=False)

#%%
#parquet
df_2 = pd.read_parquet("clientes.parquet")
df_2

#%%
#excel
df.to_excel("clientes.xlsx", index=False)

#%%
#excel
df_3 = pd.read_excel("clientes.xlsx")
df_3
#%%

df_bobo = pd.read_csv("../data/bobo.csv", sep=";")
df_bobo