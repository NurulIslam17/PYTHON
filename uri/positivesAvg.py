count=0
sum=0
for x in range(6):
    n=float(input())
    if n>0:
        count+=1
        sum+=n
avg=sum/count
print(f"{count} valores positivos\n{avg:.1f}")

