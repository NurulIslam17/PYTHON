
n=int(input())
while(n>0):
    n-=1
    player1=input()
    player2=input()

    if(player1=="ataque" and player2=="pedra"):
        print("Jogador 1 venceu")
    if (player1 == "pedra" and player2 == "ataque"):
        print("Jogador 2 venceu")

    if (player1 == "ataque" and player2 == "ataque"):
        print("Aniquilacao mutua")
    if (player1 == "pedra" and player2 == "pedra"):
        print("Sem ganhador")
    if (player1 == "papel" and player2 == "papel"):
        print("Ambos venceram")

    if (player1 == "pedra" and player2 == "papel"):
        print("Jogador 1 venceu")
    if (player1 == "papel" and player2 == "pedra"):
        print("Jogador 2 venceu")

    if (player1 == "papel" and player2 == "ataque"):
        print("Jogador 2 venceu")
    if (player1 == "ataque" and player2 == "papel"):
        print("Jogador 1 venceu")


