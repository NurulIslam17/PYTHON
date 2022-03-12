
import math
n=int(input())
m1 = ((pow((1+math.sqrt(5)),n) - pow(1-math.sqrt(5),n))/(pow(2,n)*math.sqrt(5)));
print(f"{m1:.1f}")
