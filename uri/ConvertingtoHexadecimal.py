
conversion_table=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

V=int(input())
hexaD=''
rem=1
while(V>0):
    rem=V%16
    hexaD=conversion_table[rem]+hexaD
    V=V//16
print(hexaD)
