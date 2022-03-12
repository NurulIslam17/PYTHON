
N=int(input())
suma=0
count=0
for iter in range(1,N+1):
    X,Y=map(int,input().split())
    if(X%2==0):
        X+=1
    else:
        X=X
    while(count<Y):
        suma+= X
        X+=2
        count+=1
    print(suma)
    count = 0
    suma=0
