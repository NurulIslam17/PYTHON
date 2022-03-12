
while(True):
    N=int(input())
    if(N==0):
        break
    else:
        for row in range(1,N+1):
            for col in range(1,N+1):
                print(f"{row}",end=" ")
                row*=2
            print()


