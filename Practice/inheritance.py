class Mammal:
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(f"{self.name} can Walk")

class Cat(Mammal):
    pass  # Avoiding error for empty statement

class Dog(Mammal):
   def active(self):
       print(f"{self.name} is an active animal")

dog1=Dog("Dog")
dog1.walk()
dog1.active()

cat1=Cat("Cat")
cat1.walk()