
sum,valid=0,0
while (valid<2):
    n = float(input())
    if(n>=0 and n<=10):
        sum+=n
        valid+=1
    else:
        print("nota invalida")
aveg=sum/2
print(f"media = {aveg:.2f}")
