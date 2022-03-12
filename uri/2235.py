
A,B,C=[int(x) for x in input().split()]
if(A-B==0 or A-C==0 or B-C==0):
    print("S")
elif(A+B-C==0 or B-A+C==0 or C-B+A==0):
    print("S")
elif(A-B-C==0 or A-C-B==0 or C-A-B==0):
    print("S")
else:
    print("N")