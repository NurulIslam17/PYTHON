
n=int(input())
for i in range(n):
    h,m,o=map(int,input().split(" "))

    if(h<10):
        print("0",end="")
    print(h,end="")
    print(":",end="")
    if(m<10):
        print("0",end="")
    print(m,end="")
    if(o==1):
        print(" - A porta abriu!")
    else:
        print(" - A porta fechou!")

