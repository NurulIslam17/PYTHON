
s, t, f = map(int, input().split(" "))
total = s + t + f
if (total == 24):
    print("0")
if (total < 24):
    if (total < 0):
        print(24 + total)
    else:
        print(total)
if (total > 24):
    print(total - 24)

