
x,y,z=map(int,input().split())
if (x > y and z >= y):
    print(":)")
elif (y > x and z <= y):
    print(":(")
elif (y > x and z > y and z - y < y - x):
    print(":(")
elif (y > x and z > y and z - y >= y - x):
    print(":)")
elif (x > y and y > z and z - y > y - x):
    print(":)")
elif (x > y and y > z and z - y <= y - x):
    print(":(")
elif (x == y and z > y):
    print(":)")
elif (x == y and z < y):
    print(":(")
else:
    print(":(")
