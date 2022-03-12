from random import  randint
trail=0
for attept in range(1,6):
    guess_Number=int(input("Enter the guess number ( 1 to 5) : "))
    random_Number = randint(1,5)
    if guess_Number>5 or guess_Number<=0:
        print("Enterd number is invalid.\n PLAY AGAIN")
        break
    elif random_Number==guess_Number:
        print(f"You have won. Attempt number is {attept}\n **** Congratulation ***")
        break
    else:
        trail+=1
        if trail==5:
            print("No Trails Left.\n >>> GAME OVER<<<")
        else:
            print(f"Try again. Random Number was {random_Number}")
    print(" ")