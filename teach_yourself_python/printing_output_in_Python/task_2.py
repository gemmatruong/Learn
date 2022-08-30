import time #this just allows us to work with time functions like sleep
def main():
    firstname="Mister"
    surname="Moose"
    print("Hello" + firstname + surname)
    time.sleep(1.1) #this gives a time delay
    print("Hello " + firstname + " " + surname)
    time.sleep(0.9)
    firstname="Joe"
    surname="Bloggs"
    print("Hello " + firstname + " " + surname)
    job="Coder" 
    time.sleep(0.9)
    print("Being a " + job + " is so cool")
    movie = "Shrek"
    print(movie + ", is a nice movie!")
    time.sleep(0.9)
    food = "sushi"
    color = "green"
    print("So your favorite color and food are: {} and {}.".format(color,food))
main()