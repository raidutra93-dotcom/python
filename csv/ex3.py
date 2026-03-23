import csv
arquivo_origem = 'notas.csv'
arquivo_destino = 'notas_com_media.csv'
try:
    with open(arquivo_origem, mode='r', encoding='utf-8') as csv_entrada:
        leitor = csv.DictReader(csv_entrada)
        # Define os novos cabeçalhos (originais + media)
        campos = leitor.fieldnames + ['media']       
        with open(arquivo_destino, mode='w', encoding='utf-8', newline='') as csv_saida:
            escritor = csv.DictWriter(csv_saida, fieldnames=campos)          
            # Escreve o cabeçalho no novo arquivo
            escritor.writeheader()          
            for linha in leitor:
                # Calcula a média transformando os valores em float
                n1 = float(linha['nota1'])
                n2 = float(linha['nota2'])
                n3 = float(linha['nota3'])
                media = (n1 + n2 + n3) / 3       
                # Adiciona o novo valor ao dicionário da linha
                linha['media'] = round(media, 2)      
                # Grava a linha completa no novo arquivo
                escritor.writerow(linha)
    print(f"Sucesso! O arquivo '{arquivo_destino}' foi gerado.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado.")