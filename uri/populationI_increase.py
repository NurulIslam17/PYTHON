
'''from datetime import datetime
start_time = datetime.now()'''

T=int(input())
time=0
for i in range(T):
    PA,PB,GA,GB=input().split()
    PA=int(PA)
    PB=int(PB)
    GA=float(GA)
    GB=float(GB)

    while (PA <= PB):
        PA +=(PA * GA / 100.0)
        PB +=(PB * GB / 100.0)
        time += 1

    if (time > 100):
        print("Mais de 1 seculo.")
    else:
        print(f"{time} anos.")
    time=0

'''end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))'''


