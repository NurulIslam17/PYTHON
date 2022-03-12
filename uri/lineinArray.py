l = int(input())
t = input()
sum = 0
for row in range(12):
    for col in range(12):
        x = float(input())
        if (row == l):
            sum += x
if(t=='S'):
    print(f"{sum:.1f}")
elif(t=='M'):
    avg=sum/12
    print(f"{avg:.1f}")