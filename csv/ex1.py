import csv
# Nome do arquivo de saída
arquivo = 'turma.csv'
# Abre o arquivo para escrita
with open(arquivo, mode='w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    # Escreve o cabeçalho
    escritor.writerow(['nome', 'nota1', 'nota2'])
    # Coleta os dados de 3 alunos
    for i in range(3):
        print(f"--- Aluno {i+1} ---")
        nome = input("Nome: ")
        nota1 = input("Nota 1: ")
        nota2 = input("Nota 2: ")
        # Salva a linha no CSV
        escritor.writerow([nome, nota1, nota2])
print(f"\nArquivo '{arquivo}' criado com sucesso!")