from cmath import pi


class Circle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return round(pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * pi * self.radius, 2)

c1 = Circle(13)
c2 = Circle(5)
print(c1.area())        # 530.93
print(c1.perimeter())   # 81.68
print("")
print(c2.area())        # 78.54
print(c2.perimeter())   # 31.42
