
while(True):
    try:
        t=int(input())
        if(t==0):
            break
        for i in range(t):
            n=int(input())
            if(n%2!=0):
                res=n*2-1
                print(res)
            else:
                res=n*2-2
                print(res)
    except EOFError:
        break