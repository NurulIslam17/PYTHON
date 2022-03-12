
alch,gas,dis=0,0,0
while (True):
    X = int(input())
    if(X>4):
        continue
    elif(X==4):
        break

    if(X==1):
        alch+=1
    if(X==2):
        gas+=1
    if(X==3):
        dis+=1
print("MUITO OBRIGADO")
print(f"Alcool: {alch}")
print(f"Gasolina: {gas}")
print(f"Diesel: {dis}")

