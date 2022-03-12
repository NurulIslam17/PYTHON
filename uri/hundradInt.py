n=100
high=0
pos=0
for x in range(1,n+1):
    num=int(input())
    if(high>num):
        high=high
        pos=pos
    else:
        high=num
        pos=x
print(f"{high}\n{pos}")