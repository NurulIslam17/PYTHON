N=int(input())
for i in range(N):
    n1,n2,n3=map(float,input().split())
    wAvg=(n1*2+n2*3+n3*5)
    avg=wAvg/10
    print(f"{avg:.1f}")