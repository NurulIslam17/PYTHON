sum, valid = 0, 0
while(True):
    while (valid<2):
        n = float(input())
        if(n>=0 and n<=10):
            sum+=n
            valid+=1
        else:
            print("nota invalida")
    aveg=sum/2
    print(f"media = {aveg:.2f}")
    break
print("novo calculo (1-sim 2-nao)")
new=int(input())
if(new==1):
    print()
if(new==2):
    print("")