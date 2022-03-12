x,y=map(int,input().split())
if(x<y):
    duration=y-x
else:
    duration =(24-x)+y
print(f"O JOGO DUROU {duration} HORA(S)")