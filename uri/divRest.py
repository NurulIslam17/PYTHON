
X=int(input())
Y=int(input())
if(X<Y):
    min=X
    max=Y
else:
    min=Y
    max=X
for i in range(min+1,max):
    if(i%5==2 or i%5==3):
        print(i)

