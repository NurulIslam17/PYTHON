

while(True):
    try:
        m = int(input())
        n = 0
        c = 0
        for i in range(m):
            N, C = map(int,input().split())
            c += C
            n += N*C
        print(c)
        print(n)
        intern = n / (c * 100)
        print(f"{intern:.4f}")
    except EOFError:
        break
