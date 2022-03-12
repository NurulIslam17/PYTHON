
pair=[]
impair=[]
for i in range(15):
    n=int(input())

    if n%2==0:
        pair.append(n)
    else:
        impair.append(n)

    if len(pair)==5:
        pos_After_fiveP=0
        for x in pair:
            print("par[{}] = {}".format(pos_After_fiveP,x))
            pos_After_fiveP+=1
        pair=[]

    if len(impair) == 5:
        pos_After_fiveUP = 0
        for x in impair:
            print("impar[{}] = {}".format(pos_After_fiveUP, x))
            pos_After_fiveUP += 1
        impair=[]

if len(impair) > 0:
    pos_After_fiveUP = 0
    for x in impair:
        print("impar[{}] = {}".format(pos_After_fiveUP, x))
        pos_After_fiveUP += 1

if len(pair) > 0:
    pos_After_fiveP = 0
    for x in pair:
        print("par[{}] = {}".format(pos_After_fiveP, x))
        pos_After_fiveP += 1






