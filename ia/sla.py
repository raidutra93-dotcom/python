import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('game_dataset.csv')
linhas_duplicadas = df[df.duplicated()]
print("\nLinhas duplicadas:")
print(linhas_duplicadas)
df_sem_duplicatas = df.drop_duplicates()
print("\nDataFrame sem duplicatas:")
print(df_sem_duplicatas)


mediana_classificacao = df_sem_duplicatas['Classificação de Usuários'].median()
df_sem_duplicatas['Classificação de Usuários'] = df_sem_duplicatas['Classificação de Usuários'].fillna(mediana_classificacao)

moda_idade = df_sem_duplicatas['Idade Recomendada'].mode()[0]
df_sem_duplicatas['Idade Recomendada'] = df_sem_duplicatas['Idade Recomendada'].fillna(moda_idade)

# 3. Verificar o resultado
print("\nDataFrame após o preenchimento de nulos:")
print(df_sem_duplicatas)

# Para garantir que funcionou, você pode rodar isto:
print("\nQuantidade de valores nulos restantes:")
print(df_sem_duplicatas[['Classificação de Usuários', 'Idade Recomendada']].isnull().sum())

df['Lançamento no Brasil'] = df_sem_duplicatas['Lançamento no Brasil'].map({'Sim': 1, 'Não': 0})

print("Como ficou:")
print(df_sem_duplicatas['Lançamento no Brasil'].value_counts())

# Criando colunas separadas para cada gênero e plataforma
df_transformado = pd.get_dummies(df_sem_duplicatas, columns=['Gênero',
'Plataforma'])

# Vendo as novas colunas criadas
print("Antes tínhamos uma coluna, agora temos várias:")
for coluna in df_transformado.columns:
    if coluna.startswith('Gênero_') or coluna.startswith('Plataforma_'):
        print(coluna)
print(df_transformado)

from sklearn.preprocessing import MinMaxScaler

normalizador = MinMaxScaler()

colunas_para_normalizar = ['Vendas Globais', 'Preço']

df_transformado[colunas_para_normalizar] = normalizador.fit_transform(
    df_transformado[colunas_para_normalizar]
)

print(df_transformado[colunas_para_normalizar].describe())