count=0
difference=0

while(True):
    try:
        buy_price, paid_price = map(int, input().split())

        difference=paid_price-buy_price

        if (buy_price == 0 and paid_price == 0):
            break
        if (difference >= 100):
            count += 1
            difference -= 100
        if (difference >= 50 and difference < 100):
            count += 1
            difference -= 50
        if (difference >= 20 and difference < 50):
            count += 1
            difference -= 20
        if (difference >= 10 and difference < 20):
            count += 1
            difference -= 10
        if (difference >= 5 and difference < 10):
            count += 1
            difference -= 5
        if(difference>=2 and difference<5):
            count+=1
            difference-=2

        if(count==2 and difference==0):
            print("possible")
        else:
            print("impossible")
        count=0

    except EOFError:
        break