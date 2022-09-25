import sys
class Library:
    def __init__(self, list_of_books):
        self.avail_books = list_of_books

    def display_available_books(self):
        print("The books we have in our library are as follows:")
        print("================================")
        for book in self.avail_books:
            print(book)

    def lend_book(self, requested_book):
        if requested_book in self.avail_books:
            print("The book you requested has now been borrowed")
            self.avail_books.remove(requested_book)
        else:
            print("Sorry the book you have requested is currently not in the library")

    def add_book(self, returned_book):
        self.avail_books.append(returned_book)
        print("Thanks for returning your borrowed book")


class Student:
    def __init__(self):
        self.book = None

    def request_book(self):
        print("Enter the name of the book you'd like to borrow >>>")
        self.book = input()
        return self.book

    def return_book(self):
        print("Enter the name of the book you'd like to return >>>")
        self.book = input()
        return self.book

def main():
    library = Library(["The Last Battle", "The Screwtape letters", "The Great Divorce"])
    student = Student()
    done = False
    while done is False:
        print(""" ======LIBRARY MENU=======
                1. Display all available books
                2. Request a book
                3. Return a book
                4. Exit
                """)
        choice = int(input("Enter Choice: "))
        if choice == 1:
            library.display_available_books()
        elif choice == 2:
            library.lend_book(student.request_book())
        elif choice == 3:
            library.add_book(student.return_book())
        elif choice == 4:
            sys.exit()

main()
