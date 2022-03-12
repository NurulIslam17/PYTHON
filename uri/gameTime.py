
start_hour,start_mnt,end_hour,end_mnt=map(int,input().split())

strating_mnt=(start_hour*60)+start_mnt
ending_mnt=(end_hour*60)+end_mnt

diffrent=ending_mnt-strating_mnt

if diffrent<=0:
    diffrent+=24*60
hour=diffrent//60
minutes=diffrent%60
print(f"O JOGO DUROU {hour} HORA(S) E {minutes} MINUTO(S)")