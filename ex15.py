def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    print(f"Contato {nome} adicionado!")

def buscar_contato(agenda, nome):
    resultado = agenda.get(nome, "Não encontrado")
    print(f"\nBusca por '{nome}': {resultado}")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido.")
    else:
        print("Contato não encontrado para remoção.")

def listar_contatos(agenda):
    print("\n--- Lista de Contatos (Ordem Alfabética) ---")
    if not agenda:
        print("A agenda está vazia.")
    for nome in sorted(agenda.keys()):
        print(f"{nome}: {agenda[nome]}")
    print("------------------------------------------")


minha_agenda = {}

while True:
    print("\n1. Adicionar | 2. Buscar | 3. Remover | 4. Listar | 5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        n = input("Nome: ")
        t = input("Telefone: ")
        adicionar_contato(minha_agenda, n, t)
    
    elif opcao == '2':
        n = input("Nome para buscar: ")
        buscar_contato(minha_agenda, n)
        
    elif opcao == '3':
        n = input("Nome para remover: ")
        remover_contato(minha_agenda, n)
        
    elif opcao == '4':
        listar_contatos(minha_agenda)
        
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
