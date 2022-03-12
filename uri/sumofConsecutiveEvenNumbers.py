
while(True):
    count,suma=0,0
    X = int(input())
    if(X==0):
        break
    if(X%2==0):
        X=X
    else:
        X+=1
    while(count<5):
        suma+=X
        X+=2
        count+=1
    print(suma)
    suma=0
    count=0