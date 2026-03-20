lista=[]
for i in range(1,11):
    lista.append(i)
print(lista)

for i in range(0,4):
    print(lista[i])
cont=len(lista)-1
cont2=0
while cont2<3:
    print(lista[cont])
    cont-=1
    cont2+=1
for i in range(0,len(lista)-1):
    if i%2==0:
        print(lista[i])