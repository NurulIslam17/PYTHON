
a=1
while(True):
    try:
        n1 = input()
        n2 = input()

        hit=0
        p=0
        q=0
        # print(len(n1))
        #print(len(n2))

        h=(len(n2)-len(n1))
        #print(h)
        for i in range(h+1):
            hit=0
            for j in range(len(n1)):
                if(n1[j]==n2[i+j]):
                    hit+=1
                    #print(f"hit: {hit}")
                else:
                    hit=0
                    #print(f"hitelse: {hit}")
            #print(f"final hit : {hit}")
            if(hit==len(n1)):
                q+=1
                p=i
                #print(f"quantidade: {q} pos : {p}")
        print(f"Caso #{a}:")
        if q==0:
            print("Nao existe subsequencia")
        else:
            print(f"Qtd.Subsequencias: {q}")
            print(f"Pos: {p+1}")
        print()
        a+=1
    except EOFError:
        break
