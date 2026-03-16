frase = 'o rato roeu a roupa do rei de roma'
palavras=frase.split()
p={}
for palavra in palavras:

    if palavra in p:
        p[palavra] += 1
    else:

        p[palavra] = 1


print(p)