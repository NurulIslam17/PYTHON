fruits=["Apple", "Orange","Banana"]
print(fruits)

print("-----------------")
print(fruits[2])

print("-----------------")# changing item
fruits[2]="Mango"
print(fruits)

print("-----------------")# add item
fruits.append("Banana")
print(fruits)

print(len(fruits))

print("-----------------")# loop
for x in fruits:
      print(x)

# USER INPUT LIST................
n =input('Enter the number : ')
list=n.split()
sum=0
for i in list:
      sum=sum+int(i)
print(sum)
