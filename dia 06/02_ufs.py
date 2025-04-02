#%%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(url)
uf = dfs[1]

#%%
def str_to_float(x:str):
    x = float(x.replace(" ", "")
                .replace(",", ".")
                .replace("\xa0", ""))
    return x

#%%
numero = "251 529,2"

str_to_float(numero)

#%%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

#%%
colunas = "Área (km²)", "População (Censo 2022)", "PIB (2015)", "PIB per capita (R$) (2015)"

#%%

def exp_to_anos(exp):
    return float(exp.replace("," , ".")
                    .replace(" anos", ""))
    
uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)

#%%
uf.head()

#%%
def uf_to_regiao(uf):

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)

#%%
uf.head()