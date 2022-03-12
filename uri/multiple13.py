
X=int(input())
Y=int(input())
sum=0
if(X<Y):
    min=X
    max=Y
else:
    min=Y
    max=X

for i in range(min,max+1):
    if(i%13!=0):
        sum+=i
print(sum)
