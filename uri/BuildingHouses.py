
while(True):
    X=input().split()
    if(X==['0']):
        break
    A,B,C=X
    A,B,C=int(A),int(B),int(C)

    area = A * B
    neighbor_allowed_area = (area * 100) / C
    allowed_land = (neighbor_allowed_area) ** (1 / 2)
    print(int(allowed_land))