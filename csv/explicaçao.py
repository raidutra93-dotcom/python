import csv
#cria o arquivo
dados = [
    ['nome','nota','turma'],
    ['ana',8.5,'1E'],
    ['beto',7,'1E'],
    ['carla',9,'1E'],
]

with open('turma.csv','w', encoding='utf-8',newline='')as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)
#le o aqrquivo csv

with open('turma.csv', 'r',encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for registro in leitor:
        print(registro['nome'],registro['nota1'])

