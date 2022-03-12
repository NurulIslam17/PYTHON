
T = int(input())
for i in range(T):
    name1,stat1,name2,stat2=input().split()
    N,M=input().split()
    N=int(N)
    M=int(M)
    sum=M+N
    if(sum%2==0):
        if(stat1=="PAR"):
            print(f"{name1}")
        else:
            print(f"{name2}")
    if(sum%2!=0):
        if(stat2=="IMPAR"):
            print(f"{name2}")
        else:
            print(f"{name1}")