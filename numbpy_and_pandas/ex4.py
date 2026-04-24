import numpy as np

# Objetivo: criar um array de temperaturas e analisar
temperaturas = np.array([22, 25, 19, 30, 28, 21], dtype=float)  # Forçar tipo float

media = temperaturas.mean()          # Melhor usar .mean() do que sum()/len()
print("Média:", media)

acima_media = temperaturas[temperaturas > media]
print("Acima da média:", acima_media)

# Converter Celsius para Fahrenheit
fahrenheit = temperaturas * 9/5 + 32
print("Em Fahrenheit:", fahrenheit)