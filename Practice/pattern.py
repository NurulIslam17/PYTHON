
number= int(input('Enter the number : '))
for x in range(1,number+1):
    for i in range(1,x+1):
        print(i,end=' ')
    print()

print('Pattern : 2')
for x in range(1,number+1):
    for i in range(x):
        print(x,end=' ')
    print()

print('Pattern : 3')
for x in range(1,number+1):
    for i in range(x):
        print('A',end=' ')
    print()

print('Pattern : 4')
for x in range(0,number+1):
    for i in range(x):
        print(i,end=' ')
    print()