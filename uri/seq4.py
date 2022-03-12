i,j=0,1
value=0
temp,temp1=0,0
while(i<=2):
    if(temp==0):
        print(f"I={i:.1f} J={j:.1f}")
    else:
        print(f"I={i:.1f} J={j:.1f}")

    temp+=1
    if(temp==3):
        i+= 0.2
        value += 0.2
        j=value
        temp=0
        temp1+=1
    if (temp1==5):
        temp1=0
    j+=1




