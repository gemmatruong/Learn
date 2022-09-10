from turtle import*

class Shape:
    def __init__(self, x, y):
        self.width = x
        self.height = y
    
    description = "This is an extremely important kind of shape"
    author = "No one has figured out this shape except me"
    canvas = Screen().setup(800, 800)
    turtle_obj = Turtle()

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height)*2

    def describe(self, text):
        self.description = text
    
    def author_name(self, text):
        self.author = text
    
    def scale_size(self, scale):
        self.width = self.width*scale
        self.height = self.height*scale
    
    def print_dimension(self):
        print("The dimentions of this shape are:\nWidth: {}\nHeight: {}".format(self.width, self.height))

    def draw(self):
        self.turtle_obj.forward(self.width)
        self.turtle_obj.left(90)
        self.turtle_obj.forward(self.height)
        self.turtle_obj.left(90)
        self.turtle_obj.forward(self.width)
        self.turtle_obj.left(90)
        self.turtle_obj.forward(self.height)
        self.turtle_obj.left(90)


square = Shape(100, 100)
print(square.describe("A square is a shape having 4 equal sides and 4 right angles "))
print(square.author_name("No one can tell who is the authorship of square"))
square.print_dimension()
print("The area is", square.area())
print("The perimeter is ", square.perimeter())

square.scale_size(50/100)
square.print_dimension()
print("The area is", square.area())
print("The perimeter is ", square.perimeter())
square.draw()
