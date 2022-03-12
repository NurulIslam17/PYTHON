
while(True):
    try:
        str=input()
        N=int(input())
        s=[int(i) for i in input().split()]
        n=''

        for i in s:
            n+=str[i-1]
        print(n)
    except EOFError:
        break