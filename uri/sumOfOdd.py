x=int(input())
y=int(input())
if(x<y):
    min=x+1
    max=y
else:
    min=y+1
    max=x

if (min%2==0):
    min+=1

sum=0
for i in range(min,max,2):
    sum+=i
print(sum)
