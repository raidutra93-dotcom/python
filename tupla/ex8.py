produtos = [('Camiseta', 49.90), ('Calça', 89.90), ('Tênis', 199.90)]
for e in produtos:
    nome,preço=e
    print(f'{nome}:{preço}')

nome, preço=max(produtos)
print(f'{nome}:{preço}')
