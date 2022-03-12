
n=int(input())
ans=0.0
for i in range(n):
    ans+=2
    ans=1.0/ans
ans+=1.0
print(f"{ans:.10f}")
