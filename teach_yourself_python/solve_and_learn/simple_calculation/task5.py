from cmath import pi

def create_shape():
    import turtle
    # width = int(input("Enter width: "))
    # height = int(input("Enter height: "))
    # print("You have created a shape of width:", width,"and height:", height)
    # area = width*height
    # print("The area of shape is", area)

    radius = int(input("Enter the radius of a circle: "))
    print("You have created a circle of radius:", radius)
    area = round(radius*radius*pi, 2)
    print("The area of your circle is:", area)


create_shape()