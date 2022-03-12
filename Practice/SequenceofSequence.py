
case=0
while(True):
    try:
        case+=1
        count = 1
        list = [0,]
        aux = 0
        n=int(input())
        if(n==0):
            print(f"Caso {case}: {count} numero")
            print("0")
            print()
        else:
            for i in range(1,n+1):
                if (i > aux):
                    for j in range(0,i):
                        list.append(i)
                        count+=1
            print(f"Caso {case}: {count} numeros")
            print(*list,sep=" ")
            print()
            aux=0
            count=0
    except EOFError:
        break