import numpy as np

alturas = np.array([1.65, 1.72, 1.58, 1.80, 1.68, 1.75, 1.62])   # a)
idades  = np.array([16, 17, 16, 18, 17, 17, 16])                 # b)

media_alt = alturas.mean()
std_alt   = alturas.std()          # desvio padrão
idade_max = idades.max()
idade_min = idades.min()

print(f"Média das alturas: {media_alt:.2f} m")
print(f"Desvio padrão das alturas: {std_alt:.3f} m")
print(f"Idade máxima: {idade_max} | Idade mínima: {idade_min}")

# d) Alturas de quem tem 17 anos ou mais
alturas_maiores = alturas[idades >= 17]
print("Alturas de alunos com 17+ anos:", alturas_maiores)

# e) IMC (exemplo de pesos)
pesos = np.array([58, 65, 50, 78, 62, 70, 55])  # em kg, na mesma ordem
imc = pesos / (alturas ** 2)
print("IMC dos alunos:", np.round(imc, 2))