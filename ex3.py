
nomes = ["Dipirona", "Paracetamol", "Loratadina", "Ibuprofeno", "Omeprazol"]
precos = [12.50, 9.90, 18.75, 22.00, 30.00]
estoques = [20, 15, 3, 10, 4]  


def listarMedicamentos():
    print("\n--- LISTA DE MEDICAMENTOS ---")
    for i in range(len(nomes)):
        print(f"ID: {i} | Nome: {nomes[i]} | Preço: R$ {precos[i]:.2f} | Estoque: {estoques[i]}")


def pesquisarMedicamento(nome_busca):
    encontrado = False
    for i in range(len(nomes)):
        if nomes[i].lower() == nome_busca.lower():
            print(f"\nMedicamento encontrado: {nomes[i]} | Preço: R$ {precos[i]:.2f} | Estoque: {estoques[i]}")
            encontrado = True
            break
    if not encontrado:
        print("\nMedicamento não encontrado.")


def registrarVenda(nome_medicamento, quantidade):
    if quantidade <= 0:
        print("\nErro: A quantidade deve ser maior que zero.")
        return

    indice = -1
    for i in range(len(nomes)):
        if nomes[i].lower() == nome_medicamento.lower():
            indice = i
            break

    if indice == -1:
        print("\nMedicamento não encontrado.")
        return

    if estoques[indice] >= quantidade:
        estoques[indice] -= quantidade
        print(f"\nVenda realizada com sucesso! Novo estoque de {nomes[indice]}: {estoques[indice]}")
    else:
        print("\nEstoque insuficiente para realizar a venda.")


def reporEstoque(nome_medicamento, quantidade):
    if quantidade <= 0:
        print("\nErro: A quantidade de reposição deve ser maior que zero.")
        return

    indice = -1
    for i in range(len(nomes)):
        if nomes[i].lower() == nome_medicamento.lower():
            indice = i
            break

    if indice == -1:
        print("\nMedicamento não encontrado.")
        return

    estoques[indice] += quantidade
    print(f"\nReposição realizada com sucesso! Novo estoque de {nomes[indice]}: {estoques[indice]}")

def verificarEstoqueBaixo():
    print("\n--- MEDICAMENTOS COM ESTOQUE BAIXO (< 5) ---")
    tem_baixo = False
    for i in range(len(nomes)):
        if estoques[i] < 5:
            print(f"- {nomes[i]} (Estoque atual: {estoques[i]})")
            tem_baixo = True
    if not tem_baixo:
        print("Nenhum medicamento com estoque baixo no momento.")


def menu():
    while True:
        print("\n=== MENU FARMÁCIA ===")
        print("1 - Listar medicamentos")
        print("2 - Pesquisar medicamento")
        print("3 - Registrar venda")
        print("4 - Repor estoque")
        print("5 - Mostrar estoque baixo")
        print("6 - Encerrar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            listarMedicamentos()
        elif opcao == "2":
            nome = input("Digite o nome do medicamento: ")
            pesquisarMedicamento(nome)
        elif opcao == "3":
            nome = input("Digite o nome do medicamento: ")
            qtd = int(input("Digite a quantidade a vender: "))
            registrarVenda(nome, qtd)
        elif opcao == "4":
            nome = input("Digite o nome do medicamento: ")
            qtd = int(input("Digite a quantidade a repor: "))
            reporEstoque(nome, qtd)
        elif opcao == "5":
            verificarEstoqueBaixo()
        elif opcao == "6":
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()