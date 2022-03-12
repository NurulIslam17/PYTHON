
a,b,c=map(float,input().split())
if(a<b+c and b<a+c and c<a+b):
    para=a+b+c
    print(f"Perimetro = {para:.1f}")
else:
    area=0.5*(a+b)*c
    print(f"Area = {area:.1f}")