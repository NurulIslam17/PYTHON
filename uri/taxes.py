
salary = float(input())
if (salary>=0.00 and salary<=2000.00):
    print("Isento")

elif (salary>=2000.01 and salary<=3000.00):
    amount_without_freeTaxe=salary-2000.00
    taxe=amount_without_freeTaxe*0.08
    print(f"R$ {taxe:.2f}")

elif (salary>=3000.01 and salary<=4500.00):
    amount_without_freeTaxe=salary-3000.00
    taxe=(amount_without_freeTaxe*0.18) +(1000 * 0.08)
    print(f"R$ {taxe:.2f}")
else:
    amount_without_freeTaxe = salary - 4500.00
    taxe = (amount_without_freeTaxe * 0.28) +(1500.00*.18) + (1000 * 0.08)
    print(f"R$ {taxe:.2f}")