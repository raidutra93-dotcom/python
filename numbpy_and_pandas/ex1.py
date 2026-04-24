import numpy as np
a = np.arange(1, 11)

print(a)                    # Cria array de 1 a 10 → [ 1  2  3  4  5  6  7  8  9 10]
print(a.shape)              # Retorna a dimensão do array → (10,)  (vetor de 10 elementos)
print(a[::2])               # Fatiamento com passo 2: pega elementos de índice par → [1 3 5 7 9]
print(a[::-1])              # Inverte o array → [10  9  8  7  6  5  4  3  2  1]
print(a.sum())              # Soma todos os elementos → 55
print(a.mean())             # Calcula a média aritmética → 5.5
print(a[a > 5])             # Filtra elementos maiores que 5 → [ 6  7  8  9 10]
print(a[a % 3 == 0])        # Filtra elementos divisíveis por 3 → [3 6 9]