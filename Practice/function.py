
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()
fib(10) # FUNCTION CALLING.....


num = int(input('Enter the number : '))
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)  # It is called recurssion.................
print('Factroial value is : ',fact(num)) #Return type

def add(x,y):
    sum=x+y
    return sum
'''result=add(10,20)
print('Result is ' ,result)
'''
print('Result is ',add(20,20))

