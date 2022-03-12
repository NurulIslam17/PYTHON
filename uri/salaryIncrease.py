s=float(input())
if s>=0.00 and s<=400.00:
    ns=s+(s*.15)
    me=s*.15
    ip=15
elif s>400.00 and s<=800.00:
    ns=s+(s *.12)
    me = s *.12
    ip = 12
elif s>800.00 and s<=1200.00:
    ns=s+(s*.10)
    me=s*.10
    ip=10
elif s>1200.00 and s<=2000.00:
    ns=s+ (s *.07)
    me = s*.07
    ip = 7
elif s>2000.00:
    ns=s+(s *.04)
    me = s *.04
    ip = 4
print(f"Novo salario: {ns:.2f}\nReajuste ganho: {me:.2f}")
print(f"Em percentual: {ip} %")
