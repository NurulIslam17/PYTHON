

p,j1,j2,r,a=map(int,input().split(" "))

sum=j1+j2

if ((sum % 2==0 and p==1) or (sum % 2==1 and p==0)):
    win = 1
else:
    win = 2
if((r==1 and a==0) or (r==0 and a==1)):
    win=1
elif(r==1 and a==1):
    win=2
print(f"Jogador {win} ganha!")