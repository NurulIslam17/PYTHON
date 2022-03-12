countEve=0
countOdd=0
countPos=0
countNeg=0
for i in range(5):
    n=float(input())
    if(n%2==0):
        countEve+=1
    elif(n%2!=0):
        countOdd+=1
    if(n>0):
        countPos+=1
    elif(n<0):
        countNeg+=1

print(f"{countEve} valor(es) par(es)")
print(f"{countOdd} valor(es) impar(es)")
print(f"{countPos} valor(es) positivo(s)")
print(f"{countNeg} valor(es) negativo(s)")
