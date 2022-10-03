class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def show_detail(self):
        print("This rectangle has {} inches in length and {} in width".format(self.length, self.width))
    
    def area(self):
        print("The area of this rectangle is:", self.length * self.width)

rec1 = Rectangle(5, 4)
rec2 = Rectangle(4.5, 0.8)
rec1.show_detail()
rec1.area()      # 20
rec2.area()     # 3.6