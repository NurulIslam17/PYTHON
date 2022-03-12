
number = int(input("Enter the number : "))
rev=0
temp=number
while number!=0:
    rem=number%10
    rev=(rev*10)+rem
    number=number//10

if rev==temp:
    print(f"{temp} is a Palindrome number")
else:
    print(f"{temp} is not a Palindrome number")
