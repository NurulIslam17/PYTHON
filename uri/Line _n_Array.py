
l=int(input())
t=input()

total=3
list=[]
for i in range(total):
    lista=[]
    for j in range(total):
        lista.append(float(input()))
    list.append(lista)
sum=0
for x in list[l]:
    sum+=x
result=sum
if(t== 'M'):
    result=sum/total
    print(f"{result:.1f}")
if(t== 'S'):
    print(f"{sum:.1f}")

