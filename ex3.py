lista1=[3, 17, 8, 42, 5, 100, 23, 66, 11, 99]
lista2=[]
for i in range(0,len(lista1)):
    if lista1[i]%2==0:
        print(lista1[i])
    if lista1[i]>20:
        n=lista1[i]
        lista2.append(n)
print(lista2)
soma=sum(lista1)
print(soma)
