N = int(input())
suma = 0
for i in range(N):
    X = int(input())
    for i in range(1, X + 1 // 2):
        if X % i == 0:
            suma += i
    if suma == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
    suma = 0
