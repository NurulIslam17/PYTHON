
while(True):
    try:
        N = int(input())
        M, L = [int(x) for x in input().split()]

        marcos = []
        leo = []
        for i in range(M):
            marcos.append([int(x) for x in input().split()])
        for i in range(L):
            leo.append([int(x) for x in input().split()])

        Cm, Cl = [int(x) for x in input().split()]
        A = int(input())

        marcos, leo = marcos[Cm - 1][A - 1], leo[Cl - 1][A - 1]
        # print(marcos, leo)

        if marcos > leo:
            print('Marcos')
        elif leo > marcos:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError:
        break
