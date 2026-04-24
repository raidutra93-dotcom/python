import pandas as pd
df = pd.read_csv('jogos.csv')

l,c=(df.shape)  
print(l-1)
print(df.dtypes)
print(df['nota'].mean())
print(df['preco'].mean())

print(df.loc[0:2, ['jogo', 'preco']])