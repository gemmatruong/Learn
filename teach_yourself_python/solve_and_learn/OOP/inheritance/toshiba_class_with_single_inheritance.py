class Toshiba:
    mfr = "Toshiba Inc"
    contact_website = "www.toshiba.com/contact"
    ho_location = "Minato, Tokyo, Japan"

    def contact_details(self):
        print("To contact us, simply go to", self.contact_website)

    def head_office_location(self):
        print("Our head office is located in", self.ho_location)

class ToshLaptop(Toshiba):
    def __init__(self):
        self.year_of_mfg = 2017
        self.seri_number = "#0023013"
        self.ho_location = "Minato, Tokyo, Japan"

    def manufacture_details(self):
        print(f"This Toshiba laptop was created in the year {self.year_of_mfg} by {self.mfr}")

    def serial_number(self):
        print("The serial number of this laptop is", self.seri_number)

toshiba_laptop = ToshLaptop()

toshiba_laptop.manufacture_details()
toshiba_laptop.contact_details()

laptop2 = ToshLaptop()

laptop2.head_office_location()
laptop2.serial_number()
