import numpy as np

notas = np.array([7.5, 6.0, 8.5, 7.0])

media_anual = notas.mean()                    # a) Média anual
maior_nota = notas.max()
menor_nota = notas.min()                      # b) Maior e menor nota

acima_da_media = np.sum(notas > media_anual)  # c) Quantos bimestres acima da média

notas_arredondadas = np.round(notas)          # d) Arredondamento para inteiro mais próximo

print("Média anual:", media_anual)
print("Maior nota:", maior_nota, "| Menor nota:", menor_nota)
print("Bimestres acima da média:", acima_da_media)
print("Notas arredondadas:", notas_arredondadas)