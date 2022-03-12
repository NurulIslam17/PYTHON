'''1 2 3
4 5 6
7 8 9 '''
a=[]
n,j=map(int,input().split())

for i in range(0,n):
 a.append([int(j) for j in input().split()])
