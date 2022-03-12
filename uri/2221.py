
T=int(input())
for i in range(T):
    b=int(input())

    a1,d1,l1=[int(x) for  x in input().split()]
    a2, d2, l2 = [int(x) for x in input().split()]

    Dabriel =(a1+d1)/2.0
    Guarte = (a2 + d2) / 2.0

    if(l1%2==0):
        Dabriel+=b
    if(l2%2==0):
        Guarte+=b

    if(Dabriel>Guarte):
        print("Dabriel")
    elif(Guarte>Dabriel):
        print("Guarte")
    else:
        print("Empate")