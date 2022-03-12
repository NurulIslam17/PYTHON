

while(True):
    try:
        N = int(input())
        V = input()
        V = V.count('1')
        #print(V)
        if V / N >= 2 / 3:
            print("impeachment")
        else:
            print("acusacao arquivada")

    except EOFError:
        break


