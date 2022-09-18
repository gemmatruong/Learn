class Square:
    def __init__(self, len):
        self.length = len

    def show_length(self):
        print(f"The side of this square is {self.length} in length")

    def pow(self, other):
        result = self.length ** other.length
        print("The result is:", result)


square1 = Square(2)
square2 = Square(4)

square1.show_length()
square2.show_length()
square1.pow(square2)