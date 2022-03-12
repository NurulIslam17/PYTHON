N = int(input())
for i in range(N):
    X = int(input())
    flag=0
    for divisor in range(2,X):
        if X%divisor==0:
            flag=1
            break
    if(flag==0):
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")
    flag=0

