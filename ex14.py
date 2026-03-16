info1 = {'nome': 'Notebook', 'preco': 3500.00}
info2 = {'marca': 'TechBrand', 'estoque': 15}
info3=info1 | info2
info3.update({'preco':3200})
print(info3)