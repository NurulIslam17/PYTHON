i,j=1,7
for i in range(10):
    if(i%2!=0):
        for n in range(3):
            print(f"I={i} J={j}")
            j-=1
        j=j+5

