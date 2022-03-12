

while(True):
    try:
        n = int(input())
        for row in range(1, n + 1):
            for col in range(1, n + 1):
                if (row + col == n + 1):
                    print("2", end="")
                elif (row == col):
                    print("1", end="")
                else:
                    print("3", end="")
            print()
    except EOFError:
        break
