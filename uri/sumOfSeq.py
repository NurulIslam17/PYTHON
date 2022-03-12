while (True):
    M, N = map(int, input().split())
    if(M<N):
        min=M
        max=N
    else:
        min=N
        max=M
    if (min <= 0 or max <= 0):
        break
    else:
        sum=0
        for i in range(min,max+1):
            print(i,end=" ")
            sum+=i
        print(f"Sum={sum}")

