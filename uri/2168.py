
n=int(input())
camera=[input().split() for x in range(n+1)]
    #camera=input().split()
for x in range(n):
    for y in range(n):
        if(int(camera[x][y])+int(camera[x][y+1])+int(camera[x+1][y])+int(camera[x+1][y+1])<2):
            print("U",end="")
        else:
            print("S",end="")
    print()
