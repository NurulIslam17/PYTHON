
while(True):
    try:
        A, B = map(int, input().split())
        qu = A // B
        rem = A % B
        if (rem < 0):
            if (qu < 0):
                qu = qu + 1
            if (qu > 0):
                qu = qu - 1
            rem = A - (qu * B)
        print(f"{qu} {rem}")
    except EOFError:
        break


