lista_notas=[5.0, 7.0, 4.5, 9.0, 6.0, 3.0, 8.5]

def limpar_reprovados(lista_notas):
    nova=[]
    for i in range(0,len(lista_notas)):
        if lista_notas[i]>=6:
            nova.append(lista_notas[i])
    print(nova)
limpar_reprovados(lista_notas)