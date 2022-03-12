
class Point:
    def move(self):
        print('Move method is executed')
    def draw(self):
        print("Draw method is executed")

point1=Point()
point1.draw()
point1.x=10
point1.y=20
print(point1.x)
print(point1.y)

point2=Point()
point2.move()
point2.x=20
point2.y=40
print(point2.x)
print(point2.y)