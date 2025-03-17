#%%
import pandas as pd

idades = [
    23, 29, 45, 30, 28, 
    18, 27, 29, 40, 58, 
    24, 25, 20, 23, 30
]

nomes = [
    "Samys", "Mah", "Azazel", "Mayumi", "Sodoski", 
    "Juliana", "Iara", "Gabi", "Helena", "Aurea", 
    "Ryujin", "Yeji", "Bonnie", "Natty", "Hyeri"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

#%%
df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

#%%
df["idades"]

#%%

df.iloc[0]["nomes"]
df.iloc[-1]["idades"]