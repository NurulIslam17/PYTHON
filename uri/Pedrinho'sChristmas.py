

temp=0
while(True):
    try:
        month, day = map(int, input().split())
        if(month==1):
            temp=360-day

        elif(month==2):
            temp=360-31-day

        elif (month == 3):
            temp = 360 -31-29-day

        elif (month == 4):
            temp = 360 -31-29-31- day

        elif (month == 5):
            temp = 360 -31-29-31-30-day

        elif (month == 6):
            temp = 360 -31-29-31-30-31-day

        elif (month == 7):
            temp = 360 -31-29-31-30-31-30-day

        elif (month == 8):
            temp =360-31-29-31-30-31-30-31-day

        elif (month == 9):
            temp =360-31-29-31-30-31-30-31-31-day

        elif (month == 10):
            temp =360-31-29-31-30-31-30-31-31-30-day

        elif (month == 11):
            temp =360-31-29-31-30-31-30-31-31-30-31-day

        elif (month == 12):
            temp =360-31-29-31-30-31-30-31-31-30-31-30-day


        if(temp==0):
            print(f"E natal!")
        if(temp==1):
            print(f"E vespera de natal!")
        if(temp>1):
            print(f"Faltam {temp} dias para o natal!")
        if(temp<0):
            print(f"Ja passou!")

    except EOFError:
        break