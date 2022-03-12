
N=int(input())
sumS,sumB,sumA=0,0,0
sumS1,sumB1,sumA1=0,0,0
for i in range(N):
    name=input()
    S,B,A=[int(x) for x in input().split()]
    S1,B1,A1=[int(x) for x in input().split()]

    sumS+=S
    sumB+=B
    sumA+=A

    sumS1+=S1
    sumB1+=B1
    sumA1+=A1

    resS=(sumS1/sumS)*100
    resB = (sumB1 /sumB) * 100
    resA = (sumA1 /sumA) * 100

print(f"Pontos de Saque: {resS:.2f} %.")
print(f"Pontos de Bloqueio: {resB:.2f} %.")
print(f"Pontos de Ataque: {resA:.2f} %.")


