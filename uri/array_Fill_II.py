T = int(input())
aux = 0
for i in range(10):
    print(f"N[{i}] = {aux}")
    aux += 1
    if aux == T:
        aux = 0
