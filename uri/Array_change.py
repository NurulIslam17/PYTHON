N = []
for i in range(20):
    n = int(input())
    N.append(n)
a = N[::-1]
for j in range(20):
    print("N[{}] = {}".format(j, a[j]))
