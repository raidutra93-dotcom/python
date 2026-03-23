import csv
arquivo_origem = 'notas.csv'
cabecalho = ['nome', 'media', 'situacao']
try:
    with open(arquivo_origem, mode='r', encoding='utf-8') as csv_entrada:
        leitor = csv.DictReader(csv_entrada)
        # Criamos as listas para armazenar os dados filtrados
        lista_aprovados = []
        lista_reprovados = []      
        for linha in leitor:
            media = (float(linha['nota1']) + float(linha['nota2']) + float(linha['nota3'])) / 3
            media_formatada = round(media, 2)          
            # Monta o dicionário para os novos arquivos
            novo_dado = {
                'nome': linha['nome'],
                'media': media_formatada,
                'situacao': 'Aprovado' if media >= 6 else 'Reprovado'
            }           
            if media >= 6:
                lista_aprovados.append(novo_dado)
            else:
                lista_reprovados.append(novo_dado)
    # Função auxiliar para gravar os arquivos
    def salvar_csv(nome_arquivo, dados):
        with open(nome_arquivo, mode='w', encoding='utf-8', newline='') as f:
            escritor = csv.DictWriter(f, fieldnames=cabecalho)
            escritor.writeheader()
            escritor.writerows(dados)
    salvar_csv('aprovados.csv', lista_aprovados)
    salvar_csv('reprovados.csv', lista_reprovados)
    print("Arquivos 'aprovados.csv' e 'reprovados.csv' gerados com sucesso!")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado.")