#%%
import pandas as pd

df_geral = pd.read_csv("../../data/ipea/homicidios.csv", sep=";")
df_geral = df_geral.rename(columns={"valor":"homicidios"})
df_geral.head()

#%%

df_negros = 


