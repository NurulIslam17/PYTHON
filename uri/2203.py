
from math import pow,sqrt
while(True):
    try:
        Xf, Yf, Xi, Yi, Vi, R1,R2=[int(x) for x in input().split()]

        distance=sqrt(pow((Xf-Xi),2)+pow((Yf-Yi),2))
        if(R1+R2)>=distance+1.5*Vi:
            print('Y')
        else:
            print('N')

    except EOFError:
        break