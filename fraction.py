def gcd(a, b):
    global result
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            result = i
    return result

class Fraction:
    def __init__(self, n, d):
        self.num = int(n/gcd(n, d))
        self.denom = int(d/gcd(n, d))

    def print(self):
        if self.denom == 0:
            print('Zero division error')
        elif self.num % self.denom == 0:
            print('{}'.format(self.num//self.denom))
        else:
            print ('{}/{}'.format(self.num,self.denom))

    def add(self, other):
        n = self.num*other.denom + other.num*self.denom
        d = self.denom*other.denom
        return Fraction(n, d)

    def subtract(self, other):
        n = self.num*other.denom - other.num*self.denom
        d = self.denom*other.denom
        return Fraction(n, d)

    def multiply(self, other):
        n = self.num * other.num
        d = self.denom * other.denom
        return Fraction(n, d)

    def divide(self, other):
        n = self.num * other.denom
        d = self.denom * other.num
        return Fraction(n, d)


f1 = Fraction(2, 3)
f2 = Fraction(4, 5)
f3 = Fraction(5, 0)
f4 = Fraction(-9, 2)
f5 = Fraction(4, 4)
f6 = Fraction(22, -11)

f1.print()  # 2/3
f3.print()  # Zero division error
f5.print()  # 1
f6.print()  # 5/-2
f1.add(f2).print()      # 22/15
f1.subtract(f2).print() # 8/15
f1.multiply(f2).print() # -2/15
f1.divide(f2).print()   # 5/6
f3.add(f1).print()      # Zero division error
f4.multiply(f2).print() # -18/5
