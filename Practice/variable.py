 # Variable

# Variable with name
var = 50
name = "Nurul"
print(var, end=' ')
print(name)

print('--------------------------------')
#multiple Variable
x,y,z="nurul", "Afik" , "Abrar"
print(x)
print(y)
print("Name of x is : "+z)

print('--------------------------------')
#global Variable
var = "Nurul"
def myFunc():
    print("Name is : "+var)

myFunc()

print('--------------------------------')
#casting

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

print('--------------------------------')
#get the type

var,name=20,"Nurul"
print(type(var))
print(type(name))

