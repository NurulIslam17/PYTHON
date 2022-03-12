
conversion_table=['0','1']

Dec=int(input())
binary=''
while(Dec!=0):
    rem=Dec%2
    binary=conversion_table[rem]+binary
    Dec=Dec//2
print(binary)
