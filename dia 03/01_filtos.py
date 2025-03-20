#%%
import pandas as pd

#%%
pontos = [1, 10, 50, 25, 30, 100, 50, 150, 130, 1, 0, 5, 1]
filtro = []
for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
        
resultado

#%%
df = pd.read_csv("../data/transacoes.csv")
df.head()

#%%
#pontos maiores que 50
filtro_1 = df["qtdePontos"]>=50
df[filtro_1]

#%%
# & significa and
#>= 50 e < 100
filtro_2 = (df["qtdePontos"]>=50) & (df["qtdePontos"]< 100)
df[filtro_2]

#%%
# ou 
filtro_3 = (df["qtdePontos"] == 1) | (df["qtdePontos"] == 100)
df[filtro_3]

#%%
filtro_4 = ((df["qtdePontos"] == 1 ) | (df["qtdePontos"] == 100)) & (df["dtCriacao"] >= "2025-01-01")
df[filtro_4]




