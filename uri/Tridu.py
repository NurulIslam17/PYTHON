
while (True):
    try:
        A, B = map(int, input().split())
        if(A>=B):
            print(A)
        else:
            print(B)

    except EOFError:
        break

