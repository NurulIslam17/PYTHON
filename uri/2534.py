
while(True):
    try:
        N,Q=map(int,input().split())
        grade=[]

        for i in range(N):
            n=int(input())
            grade.append(n)
        grade.sort(reverse=True)

        for j in range(Q):
            p=int(input())
            res=grade[p-1]
            print(res)
    except EOFError:
        break