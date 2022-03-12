
fraction,suma,a=0,0,1
for i in range(1,40,2):
    fraction=i/a
    a*=2
    suma+=fraction
print(f"{suma:.2f}")