#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

filtros = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtros].copy()

clientes_0["flag_1"] = 1
clientes_0
#%%
a =[1,2]
b = a.copy()
print("a", a)
print("b", b)

b.append("teste")
print("a", a)
print("b", b)

#%%
