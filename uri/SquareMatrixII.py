
while(True):
    n = int(input())
    if(n<=0):
        break
    else:
        for row in range(n):
            for col in range(n):
                if (row==col):
                    print("1", end=" ")

                elif((row+col)%2==0):
                    print(f"{n-1}",end=" ")

                elif((row+col)%2 != 0):
                    print(f"{n-2}", end=" ")
            print()