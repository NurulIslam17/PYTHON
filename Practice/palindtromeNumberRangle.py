lowerRange = int(input("Enter the lower range : "))
upperRange = int(input("Enter the upper range : "))
print('\n')
print(f"All palindrome number between { lowerRange} and {upperRange} >")
total=0
for i in range(lowerRange,upperRange+1):
    temp=i
    rev=0
    while i!=0:
        rem=i%10
        rev=(rev*10)+rem
        i=i//10
        if temp==rev:
            total=total+1
            print("   ",temp,end=" ")
print('\n')
print(f"Total palindrome number between {lowerRange} to {upperRange} is = {total}")