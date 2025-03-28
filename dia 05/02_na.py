#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes

#%%
clientes.dropna(how="any")

#%%
df = pd.DataFrame(
    {
        "nome": ["Samys", None, "Iara", "Aza"],
        "idade": [None, None, 25, 35],
        "salario": [5346, 4357, None, 3752],
    }
)
df
#%%
df.dropna(how="all", subset=["idade", "nome"])

#%%

df["idade"] = df["idade"].fillna(0)
df

#%%

df.fillna({"nome":"alguem", "idade": 0})

# %%
medias = df[["idade", "salario"]].mean()
df.fillna(medias)

# %%
df["idade"].fillna(df[["idade", "salario"]].mean()).mean()