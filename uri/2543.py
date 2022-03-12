
while(True):
    try:
        N,uID= input().split()
        count=0
        N=int(N)
        for i in range(N):
            id,j=input().split()
            if(id==uID and j=='0'):
                count+=1
        print(count)
    except EOFError:
        break

