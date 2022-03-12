T = int(input())
for tests in range(T):
    N = int(input())
    fib = [0, 1]
    if N <= 1:
        print("Fib({}) = {}".format(N, fib[N]))
    else:
        for i in range(2, N + 1):
            fib.append(fib[i - 2] + fib[i - 1])
        print("Fib({}) = {}".format(N, fib[N]))
