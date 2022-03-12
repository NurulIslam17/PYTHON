
while(True):
    try:
        count1,count2,count3=0,0,0
        L= int(input())
        for i in range(L):
            v=input().split()

            if(v<10):
                count1+=1
            elif(v>=10 and v<20):
                count2+=1
            elif(v>=20):
                count3+=1
        if(count3!=0):
            print("3")
        elif(count2!=0):
            print("2")
        else:
            print("1")
        count1, count2, count3 = 0, 0, 0

    except EOFError:
        break