#%%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv")
df.head()

#%%
df["pontos_100"] = df["qtdePontos"] + 100

df.head()

#%%
df["Email_Or_Twitch"] = df["flEmail"] + df["flTwitch"]
df.head()

#%%
df["Email_&_Twitch"] = df["flEmail"] * df["flTwitch"]
df.head()

#%%
df["Redes_Sociais"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df

#%%
df["Todas_Redes_Sociais"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] *df["flBlueSky"] * df["flInstagram"]
df

#%%
df["qtdePontos"]

#%%
df["LogPontos"] = np.log(df["qtdePontos"]+1)
df["LogPontos"].describe()

#%%
import matplotlib.pyplot as plt

plt.hist(df["LogPontos"])
plt.grid(True)
plt.show()