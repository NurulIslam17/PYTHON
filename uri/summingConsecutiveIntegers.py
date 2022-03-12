s = 0
N = list(input().split())
a = int(N[0])
b = int(N[-1])

for i in range(a, a + b):
    s += i
print(s)
