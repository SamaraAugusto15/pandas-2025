#%%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

#%%
clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%

transacoes.merge(
    right=clientes, 
    how='left', 
    on=['idCliente'],
    suffixes=["Transacao", "Cliente"]
    )