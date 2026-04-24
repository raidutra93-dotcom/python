import numpy as np

precos = np.array([19.90, 35.50, 42.00, 8.90, 120.00, 55.00])

precos_com_desconto = precos * 0.85                    # b) 15% de desconto
print("Preços com 15% de desconto:", np.round(precos_com_desconto, 2))

caros = precos_com_desconto[precos_com_desconto > 30]  # c) Acima de R$ 30 após desconto
print("Produtos acima de R$ 30 com desconto:", np.round(caros, 2))

total = precos_com_desconto.sum()                      # d) Valor total de 1 unidade de cada
print("Valor total da compra:", round(total, 2))