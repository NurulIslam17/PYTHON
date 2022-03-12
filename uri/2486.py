
while(True):
    n=int(input())
    vitamin=0
    if(n==0):
        break
    for i in range(n):
        t,name=map(str,input().split())
        name=str(name)
        t=int(t)

        if(name=='s'):
            vitamin+= 120 * t
        elif(name=='m'):
            vitamin+= 85 * t
        if (name == 'mamao'):
            vitamin += 85 * t
        if (name == 'goiaba vermelha'):
            vitamin += 70 * t
        if (name == 'manga'):
            vitamin += 56 * t
        if (name == 'laranja'):
            vitamin += 50 * t
        if (name == 'brocolis'):
            vitamin += 34 * t

    if(vitamin<110):
        vitamin= 110 - vitamin
        print(vitamin)
    elif (vitamin > 130):
        vitamin = vitamin - 130
        print(vitamin)
    else:
        print(vitamin)
