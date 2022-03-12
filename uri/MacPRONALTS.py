

n=int(input())
sum=0
for i in range(n):
    x,y=input().split()
    x=int(x)
    y=int(y)
    if(x==1001):
        sum=sum+(1.50*y)
    if (x == 1002):
        sum = sum + (2.50 * y)
    if (x == 1003):
        sum = sum + (3.50 * y)
    if (x == 1004):
        sum = sum + (4.50 * y)
    if (x == 1005):
        sum = sum + (5.50 * y)
print(f"{sum:.2f}")

