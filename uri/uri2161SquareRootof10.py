
n=int(input())
ans=0.0

for i in range(n):
    ans+=6.0
    ans=1.0/ans
ans+=3.0
print(f"{ans:.10f}")
