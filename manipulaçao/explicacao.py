#sobreescreve o arquivo com w 
with open('teste.txt','w',encoding='utf-8') as manipulaçao:
    manipulaçao.write('primeira linha\n')
    manipulaçao.write('segunda linha\n')

#adiciona no fim com a 
with open('teste.txt','a',encoding='utf-8') as manipulaçao:
    manipulaçao.write('terceira linha\n')

#lendo arquivo com r
with open('teste.txt','r',encoding='utf-8') as manipulaçao:
    #le inteiro com string
    #conteudo=manipulaçao.read()
    #print(conteudo)

    #le separadamente por for
    #for linha in manipulaçao:
    #    print(linha.strip())

    # Ler todas as linhas como lista
    linhas = manipulaçao.readlines()
    print(linhas) 
