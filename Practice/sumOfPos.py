
number = int(input("Enter the Limits : "))
sum=0
for x in range(2,number+1,2):
    sum+=x
    print(x,end="+")
print(" = ",sum)