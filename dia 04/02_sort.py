#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")

max_pontos = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_pontos
clientes[filtro]

#%%
(clientes.sort_values(by="qtdePontos", ascending=False)
        .head(5)["idCliente"])

#%%
clientes

#%%

brinquedo = pd.DataFrame(
    {
        "nome": ["Samys","Aza", "Mayumi", "Iara"],
        "idade": [23, 35, 30, 25],
        "salario": [2423, 4133, 5123, 4133],
    }
)

brinquedo

#%%
#maior salario e maior idade
brinquedo.sort_values(by=["salario", "idade"], ascending=False)

#%%
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])

