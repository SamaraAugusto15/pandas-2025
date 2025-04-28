# %%
import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

#%%
def diff_amp(x:pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media)**2)

idades = pd.Series([21,23,54,15,75,75,15,72,62,41])

#%%

(transacoes.groupby(by=["idCliente"])
            .agg({
                "idTransacao":['count'],
                "qtdePontos": ['sum','mean', diff_amp]
            })
)





