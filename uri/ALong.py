
N = int(input())
for i in range(N):
    T = int(input())
    T=2015-T
    if(T<1):
        time=1-T
        print(f"{time} A.C.")
    else:
        print(f"{T} D.C.")