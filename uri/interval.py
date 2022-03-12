N=int(input())
iN=0
out=0
for i in range(N):
    x=int(input())
    if(x>=10 and x<=20):
        iN+=1
    else:
        out+=1
print(f"{iN} in\n{out} out")
