#%%
import pandas as pd

#%%
df = pd.read_csv("../data/clientes.csv")

#%%
#para converter .astype
df["qtdePontos"].astype(float).astype(str)