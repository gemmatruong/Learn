class Furniture:
    type_of_wood = "oak"

    def show_wood(self):
        print("The wood of this furniture comes from:", self.type_of_wood)

class Wardrobe(Furniture):
    def __init__(self):
        self.height = '79.25"'

    def show_height(self):
        print("The height of this wardrobe is:", self.height)

    def change_wood(self):
        print("Please enter the wood of wardrobe that you like >>>")
        self.type_of_wood = input()
        print("Type of wood has been changed")


if __name__ == "__main__":
    wardrobe1 = Wardrobe()
    wardrobe1.change_wood()
    wardrobe1.show_wood()
    wardrobe1.show_height()
