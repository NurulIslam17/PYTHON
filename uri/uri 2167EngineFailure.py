
n=int(input())
L=[]
L=input().split()
pos=0
for i in range(1,n):
    if(int(L[i-1])>int(L[i])):
        pos=i+1
        break
print(pos)


