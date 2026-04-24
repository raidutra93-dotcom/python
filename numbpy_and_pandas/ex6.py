import numpy as np

def simular_dado(n):
    lancamentos = np.random.randint(1, 7, size=n)
    media = lancamentos.mean()
    valores, contagens = np.unique(lancamentos, return_counts=True)
    porc_6 = (contagens[5] / n) * 100 if 6 in valores else 0
    
    print(f"\n--- {n} lançamentos ---")
    print(f"Média: {media:.4f}")
    print("Frequência de cada face:", dict(zip(valores, contagens)))
    print(f"Porcentagem de 6: {porc_6:.2f}%")
    return media

# Simulações
for tamanho in [10, 100, 1000, 100000]:
    simular_dado(tamanho)