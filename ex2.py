
def registrarTentativas():
    tentativas = []
    i = 0
    print("Digite o resultado de cada tentativa (0, 1, 2 ou 3):")
    
    while i < 10:
        try:
            valor = int(input(f"Tentativa {i + 1}: "))
            if valor in [0, 1, 2, 3]:
                tentativas.append(valor)
                i += 1
            else:
                print("Valor inválido! Digite apenas 0, 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    return tentativas



def calcularPontuacao(tentativas):
    return sum(tentativas)



def calcularAproveitamento(tentativas):
    acertos = 0
    errados = 0
    
    for t in tentativas:
        if t == 0:
            errados += 1
        else:
            acertos += 1
            
    
    percentual = (acertos / len(tentativas)) * 100
    
    print(f"Arremessos convertidos: {acertos}")
    print(f"Arremessos errados: {errados}")
    print(f"Percentual de aproveitamento: {percentual:.1f}%")



def encontrarCestaMaisFrequente(tentativas):
    cont1 = tentativas.count(1)
    cont2 = tentativas.count(2)
    cont3 = tentativas.count(3)
    
    if cont1 == 0 and cont2 == 0 and cont3 == 0:
        return "Nenhuma cesta foi convertida."
    
    mais_frequente = "1 ponto"
    max_freq = cont1
    
    if cont2 > max_freq:
        max_freq = cont2
        mais_frequente = "2 pontos"
    if cont3 > max_freq:
        max_freq = cont3
        mais_frequente = "3 pontos"
        
    return f"O tipo de cesta mais frequente foi de {mais_frequente} ({max_freq} vezes)."



if __name__ == "__main__":
    print("=== ANÁLISE DE ARREMPESSOS DE BASQUETE ===")
    dados_tentativas = registrarTentativas()
    
    print("\n--- RELATÓRIO FINAL ---")
    print(f"Pontuação Total: {calcularPontuacao(dados_tentativas)}")
    calcularAproveitamento(dados_tentativas)
    print(encontrarCestaMaisFrequente(dados_tentativas))