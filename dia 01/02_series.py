#%%

idades = [
    23, 25, 45, 30, 36, 
    19, 33, 29, 40, 31, 
    35, 14, 27, 42, 33
]

media = sum(idades) / len(idades)
print("Media:",media)


diffs = 0
for i in idades:
    diffs += (i - media) ** 2
    
variancia = diffs/(len(idades)-1)
print("Variancia: ",variancia)

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
#estatistica das series
media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()
summary_idades