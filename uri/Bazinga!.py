
T=int(input())
win=""
for i in range(T):
    seldnOP, rajOP=input("").split()
    if seldnOP==rajOP:
        win="De novo!"

    elif seldnOP== "pedra":
        if(rajOP=="tesoura" or rajOP=="lagarto"):
            win=seldnOP
        else:
            win=rajOP

    elif seldnOP== "papel":
        if(rajOP=="pedra" or rajOP=="Spock"):
            win=seldnOP
        else:
            win = rajOP

    elif seldnOP== "tesoura":
        if(rajOP=="papel" or rajOP=="lagarto"):
            win=seldnOP
        else:
            win=rajOP

    elif seldnOP== "lagarto":
        if(rajOP=="Spock" or rajOP=="papel"):
            win=seldnOP
        else:
            win=rajOP

    elif seldnOP == "Spock":
        if (rajOP == "tesoura" or rajOP == "pedra"):
            win = seldnOP
        else:
            win = rajOP

    if(win==seldnOP):
        win="Bazinga!"
    elif(win==rajOP):
        win="Raj trapaceou!"
    print(f"Caso #{i+1}: {win}")