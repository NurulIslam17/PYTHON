

while(True):
    try:
        x, y = map(int, input().split(":"))
        if (x < 7 or (x == 7 and y == 0)):
            print(f"Atraso maximo: {0}")
        else:
            res = ((x + 1) - 8) * 60 + y
            print(f"Atraso maximo: {res}")
    except EOFError:
        break
