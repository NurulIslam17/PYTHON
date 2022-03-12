
while (True):
    X=int(input())
    if(X==0):
        break
    else:
        for i in range(1,X+1):
            print(i,end="")
            if(i!=X):
                print(end=" ")
        print()