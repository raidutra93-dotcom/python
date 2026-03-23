def contar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
            num_linhas = len(linhas)
            num_palavras = 0
            
            for linha in linhas:
                # O split() sem argumentos lida automaticamente com espaços e quebras de linha
                palavras = linha.split()
                num_palavras += len(palavras)
            
            print(f"a) O arquivo tem {num_linhas} linhas.")
            print(f"b) O arquivo tem {num_palavras} palavras no total.")
            
    except FileNotFoundError:
        print("Erro: O arquivo 'diario.txt' não foi encontrado.")

# Executa a função
contar_arquivo('diario.txt')