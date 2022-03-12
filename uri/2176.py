

n=input()
count=0
l=len(n)
for i in range(0,l):
    if(n[i]=='1'):
        count+=1
if(count%2==0):
    n=n+'0'
else:
    n=n+'1'
print(n)