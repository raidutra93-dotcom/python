import pandas as pd
df = pd.read_csv('jogos.csv')

df['genero'].value_counts()         # Minha previsão:2 sandbox
df['nota'].max()                   # Minha previsão:93
df['preco'].min()                   # Minha previsão:82
df.loc[5, 'jogo']                    # Minha previsão:minecraft
df.iloc[0:3, 1:3]                     # Minha previsão:
print(df[['jogo', 'ano']].tail(3)    )        # Minha previsão:cs 2012, clash royale, 2016, jogo, 2022
print(df.describe().loc['mean'] )           # Minha previsão:error
