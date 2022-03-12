

while(True):
    n = int(input())
    if(n<=0):
        break
    else:
        for row in range(n):
            for col in range(n):
                if (row == 0 or col == 0 or row == n - 1 or col == n - 1):
                    print("1", end=" ")
                else:
                    print("2", end=" ")
            print()