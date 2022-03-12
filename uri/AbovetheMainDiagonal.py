
o=input()
count=0
sum=0
for row in range(12):
    for col in range(12):
        x=float(input())
        if(row<col):
            sum+=x
            count+=1
if(o=='S'):
    print(f"{sum:.1f}")
elif(o=='M'):
    avg=sum/count
    print(f"{avg:.1f}")

