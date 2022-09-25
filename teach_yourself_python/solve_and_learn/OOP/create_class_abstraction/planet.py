from turtle import*

class Planet:
    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y

    canvas = Screen().setup(1500,1000)
    turtle = Turtle()

    def circumference(self):
        return 2*3.1415*self.radius

    def scale_size(self, scale):
        self.radius = self.radius*scale

    def draw(self, colour):
        self.turtle.goto(self.x, self.y) #go to (x,y + radius)
        self.turtle.color(colour)
        self.turtle.dot(self.radius)


planet1 = Planet(-200, -100, 200)
planet1.draw("red")
print("Circumference *check the maths!* is:", planet1.circumference())
planet1.scale_size(0.5)
planet1.draw("yellow")

planet2 = Planet(300, 300, 100)
planet2.draw("black")

planet3 = Planet(-300, 200, 150)
planet3.draw("green")
planet3.scale_size(0.75)
planet3.draw("white")

planet4 = Planet(300, -100, 400)
planet4.draw("blue")
planet4.scale_size(0.25)
planet4.draw("white")
