number=int(input("Enter the number you want to check : "))
divisor=2
flag=0
for divisor in range(2,number//2):
    if number%divisor==0:
        flag=1
        break
if number==1:
    print(f"{number} is neither Prime nor composite")
else:
    if flag==0:
        print(f"{number} is Prime")
    else:
        print(f"{number} is not a Prime")

