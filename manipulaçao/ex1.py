with open('frutas.txt','w',encoding='utf-8') as manipulaçao:
    manipulaçao.write('banana\n')
    manipulaçao.write('berinjela\n')
    manipulaçao.write('cenoura\n')
    manipulaçao.write('pepino\n')
    manipulaçao.write('abacaxi\n')

with open('frutas.txt','r',encoding='utf-8') as manipulaçao:
    #le separadamente por for
    for linha in manipulaçao:
        print(linha.strip())