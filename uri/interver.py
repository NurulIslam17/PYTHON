A=float(input())
if A<0 or A>100:
    print("Fora de intervalo")
else:
    if A>=0 and A<=25:
        print(f"Intervalo [0,25]")
    elif A>25 and A<=50:
        print(f"Intervalo (25,50]")
    elif A>50 and A<=75:
        print(f"Intervalo (50,75]")
    elif A>75 and A<=100:
        print(f"Intervalo (75,100]")




