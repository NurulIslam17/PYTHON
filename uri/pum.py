N = int(input())
cont = 0
A, B, C = 1, 2, 3
while cont < N:
    print('{0} {1} {2} PUM'.format(A, B, C))
    C+=2

    A = C
    B = A+1
    C=B+1

    cont+=1
