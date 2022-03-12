
N,M=map(int,input().split())
tab=0
for i in range(M):
    x=input()
    if(x=="fechou"):
        N+=1
    else:
        N-=1
print(N)