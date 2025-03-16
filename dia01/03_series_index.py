#%%
import pandas as pd

idades = [
    23, 25, 45, 30, 36, 
    19, 33, 29, 40, 31, 
    35, 14, 27, 42, 33
]

series_idades = pd.Series(idades)
series_idades

#%%
idades[0]
series_idades[0]

#%%
#ordenou por idade
series_idades = series_idades.sort_values()
series_idades

#%%
#indice no sentido de posição n como chave
prim_pos = series_idades.iloc[0]
print(prim_pos)
ultm_pos = series_idades.iloc[-1]
print(ultm_pos)

#%%
series_idades.iloc[:3]

#%%
series_idades.iloc[::-1]

#%%

idades = [
    23, 25, 45, 30, 36, 
    19, 33, 29, 40, 31, 
    24, 25, 27, 23, 30
]

indexs = [
    "Samys", "Mah", "Azazel", "Mayumi", "Sodoski", 
    "Juliana", "Iara", "Gabi", "Helena", "Aurea", 
    "Ryujin", "Yeji", "Bonnie", "Natty", "Hyeri"
]

series_idades = pd.Series(idades, index=indexs)
series_idades

#%%
series_idades["Samys"]
series_idades.loc["Ryujin"]
#%%
series_idades.iloc[-1]