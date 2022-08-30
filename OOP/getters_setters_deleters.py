class skin_care_routine:
    def __init__(self,prod,price,qty):
        self.product = prod
        self.price = price
        self.quantity = qty
        self.expense = price*qty
    
    @property
    def expense_per_year(self):
        return self.price * self.quantity
    
    @expense_per_year.setter
    def expense_per_year(self, new_expense):
        new_price, new_quantity = map(int,new_expense.split('x'))
        self.price = new_price
        self.quantity = new_quantity

    @expense_per_year.deleter
    def expense_per_year(self):
        self.price = 0
        self.quantity = 0
        print('Deleted!')

step1 = skin_care_routine('Centaphil',14,2)
step1.price = 16

step1.expense_per_year = '20x3'

print(step1.product)
print(step1.price)
print(step1.quantity)
del step1.expense_per_year
print(step1.expense)
print(step1.expense_per_year)
print(step1.price)
print(step1.quantity)



