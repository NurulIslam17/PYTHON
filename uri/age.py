
suma,avg=0,0
count=0
while(True):
    age=int(input())
    if(age>=0):
        suma += age
        count += 1
        avg = suma / count
        continue
    print(f"{avg:.2f}")
    break
