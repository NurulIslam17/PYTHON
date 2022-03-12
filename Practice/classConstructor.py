
# constructor is a function that get called at  the time of creating an object
class Point:
    def __init__(self,x,y): #Constructor......
        self.x=x
        self.y=y

    def move(self):
        print('Move method is executed')
    def draw(self):
        print("Draw method is executed")

point = Point(10,20)
print(point.x)
print(point.y)