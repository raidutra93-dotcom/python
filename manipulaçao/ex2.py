with open('compras.txt','w',encoding='utf-8') as manipulaçao:
    while True:
        b = input("vai escolher algo  se n degite 'n'")

        if b == ("n"):
            break 
        else:
                manipulaçao.write(f"{b}\n")
with open('compras.txt','r',encoding='utf-8') as manipulaçao:
    #le inteiro com string
    #conteudo=manipulaçao.read()
    #print(conteudo)

    #le separadamente por for
    for linha in manipulaçao:
        print(linha.strip())

    # Ler todas as linhas como lista
    #linhas = manipulaçao.readlines()
    #print(linhas) 
