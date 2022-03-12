
a,b=map(int,input().split())
for rem in range(abs(b)):
    if((a-rem)%b==0):
        q=int((a-rem)/b)
        break
print(q,rem)