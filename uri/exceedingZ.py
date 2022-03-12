X=int(input())
count=0
add=0
while(True):
    Z = int(input())
    if(Z<=X):
        continue
    else:
        while(add<Z):
            add+=X
            X+=1
            count+=1
    print(count)
    break


