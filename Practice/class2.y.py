class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi! I am {self.name}")
    def walk(self):
        print(f"Lets walk {self.name}")

nurul=Person("Nurul Islam")
nurul.talk()
bob = Person("Bob Smith")
bob.talk()
bob.walk()