
while(True):
    try:
        v=float(input())
        d=float(input())

        r=d/2
        a=3.14*r*r
        h=v/a

        print(f"ALTURA = {h:.2f}")
        print(f"AREA = {a:.2f}")
    except EOFError:
        break