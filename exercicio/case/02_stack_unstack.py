#%%
import pandas as pd

df = pd.read_csv("homicidios_consolidado.csv", sep=";")
df.head()

# %%
df_stack = (df.set_index(["nome", "período"])
        .stack())
df_stack = df_stack.reset_index()
df_stack.columns =["nome", "período", "metrica", "valor"]
df_stack

#%%
