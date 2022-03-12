
N=int(input())
X=list(map(int,input().split()))
location=0
minimum=X[0]
count=0
for i in X:
    if i<minimum:
        minimum=i
        location=count
    count+=1
print(f"Menor valor: {minimum}")
print(f"Posicao: {location}")