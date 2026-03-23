import csv
arquivo_nome = 'notas.csv'
try:
    with open(arquivo_nome, mode='r', encoding='utf-8') as arquivo:
        # a) Leia o arquivo usando csv.DictReader
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            nome = linha['nome']
            # b) Calcule a média das três notas
            n1 = float(linha['nota1'])
            n2 = float(linha['nota2'])
            n3 = float(linha['nota3'])
            print(f"{nome:<10} | {n1:<6} | {n2:<6} | {n3:<6}")           
            media = (n1 + n2 + n3) / 3           
            # c) Imprima o status (Aprovado se média >= 6)
            status = "Aprovado(a)" if media >= 6 else "Reprovado(a)"           
            # Formatação: .2f limita a 2 casas decimais
            print(f"{nome} – Média: {media:.2f} – {status}")
            print('----'*20)
except FileNotFoundError:
    print(f"Erro: Certifique-se de que o arquivo '{arquivo_nome}' foi criado.")