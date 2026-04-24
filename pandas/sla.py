import pandas as pd
 
dados = {
    'jogo': ['The Witcher 3', 'Celeste', 'Hades', 'Stardew Valley', 'Hollow Knight'],
    'genero': ['RPG', 'Plataforma', 'Roguelike', 'Simulação', 'Metroidvania'],
    'nota_metacritic': [93, 91, 93, 89, 90],
    'preco_reais': [79.90, 36.99, 46.99, 24.99, 27.99],
    'ano_lancamento': [2015, 2018, 2020, 2016, 2017]
}
 
df = pd.DataFrame(dados)
print(df)