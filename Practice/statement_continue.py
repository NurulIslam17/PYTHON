num=int(input("Enter the number : "))
even,odd=0,0
for n in range(2,num):
    if n%2==0:
        print('Found a even number',n)
        even=even+1
        continue
    print("Found a Odd nunmber ",n);
    odd=odd+1
print('-------------Count-------------')
print('Even =',even)
print('Odd=',odd)