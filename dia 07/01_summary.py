#%%
import pandas as pd

idades = [32,44,15,54,67,32,23,34,14,45,43,28,73,29]

idades = pd.Series(idades)
idades

# %%
idades.sum()

# %%
idades.min()

# %%
idades.max()

# %%
idades.mean()