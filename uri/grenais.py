i,g,e=0,0,0
while (True):
    x,y = map(int,input().split())
    print("Novo grenal (1-sim 2-nao)")

    if(x>y):
        i+=1
    if (x<y):
        g+=1
    if(x==y):
        e+=1

    selc=int(input())
    if(selc==1):
        continue
    if (selc==2):
        break

total=i+g+e
print(f"{total} grenais")
print(f"Inter:{i}")
print(f"Gremio:{g}")
print(f"Empates:{e}")

if(i>g):
    print("Inter venceu mais")
if(i<g):
    print("Gremio venceu mais")
if(i==g):
    print("Não houve vencedor")
