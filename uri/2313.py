
from math import pow
a,b,c=map(int,input().split())
if(a+c>b):
    if (a != b and b == c) or (a != b and a == c) or (c != b and a == b):
        res = 'Valido-Isoceles'
    elif (a == b and a == c):
        res = 'Valido-Equilatero'
    elif (a != b and b != c and a != c):
        res = 'Valido-Escaleno'
else:
    res='Invalido'

if(res!='Invalido'):
    if(pow(a,2)==pow(b,2)+pow(c,2) or pow(b,2)==pow(a,2)+pow(c,2) or pow(c,2)==pow(b,2)+pow(a,2)):
        print(res)
        print('Retangulo: S')
    else:
        print(res)
        print('Retangulo: N')
else:
    print(res)
