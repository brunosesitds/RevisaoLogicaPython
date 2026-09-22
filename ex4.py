# Matriz 5x6 inicializada com "L" (Livre)
# Linhas 0 a 4 correspondem às fileiras 1 a 5
# Colunas 0 a 5 correspondem de A a F
matriz_assentos = [["L" for _ in range(6)] for _ in range(5)]

# Dicionários para mapear colunas
colunas_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

# 1. Mostrar assentos
def mostrarAssentos():
    print("\n     A    B    C    D    E    F")
    for i in range(5):
        linha_str = f"{i+1} "
        for j in range(6):
            linha_str += f"   {matriz_assentos[i][j]}"
        print(linha_str)

# 2. Validar assento
def validarAssento(codigo):
    codigo = codigo.upper().strip()
    if len(codigo) != 2:
        return None
    
    char_linha = codigo[0]
    char_coluna = codigo[1]
    
    if not char_linha.isdigit() or not char_coluna.isalpha():
        return None
        
    linha = int(char_linha) - 1
    coluna = colunas_map.get(char_coluna)
    
    if linha < 0 or linha > 4 or coluna is None:
        return None
        
    return (linha, coluna)

# 3. Verificar disponibilidade
def verificarDisponibilidade(linha, coluna):
    return matriz_assentos[linha][coluna] == "L"

# 4. Calcular preço e categoria
def calcularPreco(linha):
    if linha == 0:
        return "Executiva", 850.0
    elif linha in (1, 2):
        return "Espaço extra", 600.0
    else:
        return "Econômica", 400.0

# Comprar assento (integra validação, preço, confirmação e atualização)
def comprarAssento():
    codigo = input("Assento desejado (ex: 2C): ")
    pos = validarAssento(codigo)
    
    if pos is None:
        print("\nAssento inválido! Verifique a fileira (1-5) e a coluna (A-F).")
        return
        
    linha, coluna = pos
    
    if not verificarDisponibilidade(linha, coluna):
        print(f"\nO assento {codigo.upper()} já está ocupado.")
        print("Escolha outro assento.")
        return
        
    categoria, preco = calcularPreco(linha)
    
    print(f"\nAssento desejado: {codigo.upper()}")
    print(f"Categoria: {categoria}")
    print(f"Valor: R$ {preco:.2f}")
    
    confirmar = input("Confirmar compra? (S/N): ").strip().upper()
    if confirmar == 'S':
        matriz_assentos[linha][coluna] = "O"
        print(f"\nCompra realizada com sucesso.")
        print(f"O assento {codigo.upper()} agora está indisponível.")
    else:
        print("\nCompra cancelada.")

# Consultar status de um assento específico
def consultarAssento():
    codigo = input("Digite o assento que deseja consultar (ex: 1A): ")
    pos = validarAssento(codigo)
    if pos is None:
        print("\nAssento inválido!")
        return
    linha, coluna = pos
    status = "Livre" if matriz_assentos[linha][coluna] == "L" else "Ocupado"
    categoria, preco = calcularPreco(linha)
    print(f"\nAssento: {codigo.upper()} | Status: {status} | Categoria: {categoria} | Preço: R$ {preco:.2f}")

# 6. Mostrar resumo do voo
def mostrarResumo():
    livres = 0
    ocupados = 0
    faturamento = 0.0
    
    vendas_categoria = {
        "Executiva": 0,
        "Espaço extra": 0,
        "Econômica": 0
    }
    
    for i in range(5):
        for j in range(6):
            categoria, preco = calcularPreco(i)
            if matriz_assentos[i][j] == "L":
                livres += 1
            else:
                ocupados += 1
                faturamento += preco
                vendas_categoria[categoria] += 1
                
    total_assentos = 30
    percentual = (ocupados / total_assentos) * 100
    
    print("\n=== RESUMO DO VOO ===")
    print(f"Quantidade de assentos livres: {livres}")
    print(f"Quantidade de assentos ocupados: {ocupados}")
    print(f"Percentual de ocupação: {percentual:.1f}%")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print("Vendas por categoria:")
    for cat, qtd in vendas_categoria.items():
        print(f"  - {cat}: {qtd} assento(s)")

# Menu principal
def menu():
    while True:
        print("\n=== SISTEMA DE COMPRA DE PASSAGENS ===")
        print("1 - Visualizar assentos")
        print("2 - Comprar assento")
        print("3 - Consultar assento")
        print("4 - Mostrar resumo do voo")
        print("5 - Encerrar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            mostrarAssentos()
        elif opcao == "2":
            comprarAssento()
        elif opcao == "3":
            consultarAssento()
        elif opcao == "4":
            mostrarResumo()
        elif opcao == "5":
            print("\nEncerrando o sistema. Tenha um ótimo dia!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()