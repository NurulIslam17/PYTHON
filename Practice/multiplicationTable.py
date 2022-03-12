
number=int(input("Enter  Table Header : "))
limit=0
print(f"Multiplication table for {number}")
while limit<=10:
    mult=number*limit
    print(f"{number} * {limit} = {mult}")
    limit=limit+1

