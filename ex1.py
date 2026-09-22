gols = []
jogadores = []


def registrar():
    for i in range(0, 5):
        nomeJogador = input("Qual o nome do jogador?\n")
        jogadores.append(nomeJogador)
        golsJogador = input("Quantos gols tem o jogador?\n")
        gols.append(int(golsJogador))
        print("\n")

def totalGolsTime():
    soma = 0

    for i in range(0, 5):
        soma += gols[i]

    return soma

def calcularArtilheiro():
    artilheiro = jogadores[0]
    indexArtilheiro = 0

    for i in range(1, 5):
        if(gols[i] > gols[indexArtilheiro]):
            artilheiro = jogadores[i]
           
    return artilheiro

def calcularIndexArtilheiro():
    artilheiro = jogadores[0]
    indexArtilheiro = 0

    for i in range(1, 5):
        if(gols[i] > gols[indexArtilheiro]):
            artilheiro = i
           
    return artilheiro

def verificarEmpateArtilharia():
    artilheiroPrincipal = calcularArtilheiro()

    artilheiro = jogadores[0]
    indexArtilheiro = calcularIndexArtilheiro()

    temUmcaba = False

    for i in range(1, 5):
        if(gols[i] >= gols[indexArtilheiro]):
            artilheiro = i
            if(artilheiroPrincipal != jogadores[i]):
                temUmcaba = True
   
    return temUmcaba

def jogadoresComGolsAcimaDaMedia():
    for i in range(1, 5):
        if(gols[i] >= totalGolsTime() / 5):
            print(f" - {jogadores[i]}")

def printarJogadores():
    for i in range(0, 5):
        print(f"{jogadores[i]} - {gols[i]} gols")

registrar()

printarJogadores()
print(f"Total de gols do time {totalGolsTime()}")
print(f"Media de gols do time por jogador {totalGolsTime() / 5}")
print("Jogadores com mais gols que a media : ")
jogadoresComGolsAcimaDaMedia()
print(f"Artilheiro {calcularArtilheiro()}, empate na artilharia? {verificarEmpateArtilharia()}")