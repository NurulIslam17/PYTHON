

n=int(input())
for i in range(n):
    reg,note=input().split()
    reg=int(reg)
    note=float(note)
    if(note<8):
        print("Minimum note not reached")
    else:
        print()