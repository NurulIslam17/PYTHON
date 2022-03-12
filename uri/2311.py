
N=int(input())
for i in range(N):
    name=input()
    dificulty=float(input())
    s=[float(x) for x in input().split()]
    s=sum(sorted(s)[1:6])*dificulty
    print('%s %.2f' % (name,s))
