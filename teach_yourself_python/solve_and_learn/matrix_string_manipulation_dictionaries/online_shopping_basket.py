import sys

products_info = ["001", "iphone", "£900", "002", "samsung", "£1020", "003", "toshiba", "£700", "004", "toyota", "£2100", "005", "cetaphil", "£10"]
viewing_basket = []

def main():
    print("""
============== MAIN MENU =====================
    1 - Browse products in our store
    2 - View basket
    3 - Checkout
    4 - Quit
    """)
    choice = input("Enter choice: ")
    if choice == "1":
        browse_products()
    elif choice == "2":
        view_basket()
    elif choice == "3":
        checkout()
    elif choice == "4":
        sys.exit()
    else:
        print("Please enter valid choice")


def browse_products():
    print("====== BROWSE PRODUCTS IN OUR STORE ============")
    code = input("Enter the product code of an item: ")
    if code in products_info:
        i = products_info.index(code)
        print("Product name:", products_info[i+1])
        print("Product cost:", products_info[i+2])
        viewing_basket.append([products_info[i+1], products_info[i+2]])
        print("")
        print("This item has been added to your viewing basket")
    else:
        print("Product not found")
    main()


def view_basket():
    print("=======================Your basket========================")
    for ele in viewing_basket:
        print(ele)
    main()


def checkout():
    total = []
    for ele in viewing_basket:
        total.append(int(ele[1].lstrip("£")))
    print("Your total checkout cost is:", sum(total))
    main()


main()
