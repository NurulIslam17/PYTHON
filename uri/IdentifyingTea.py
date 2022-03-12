
T=int(input())
count=0
x1,x2,x3,x4,x5=map(int,input().split())
if(T==x1):
    count+=1
if(T==x2):
    count += 1
if(T==x3):
    count+=1
if(T==x4):
    count += 1
if(T==x5):
    count+=1

print(count)