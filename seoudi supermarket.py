import sys

class Product:
    supermarket_name = "seoudi"

    def __init__(self, product_id, name, price, manufacturer, weight, expiration_date, year):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, new_id):
        self.__product_id = new_id
        print("Product ID updated successfully.\n")

    def product_detail(self):
        print("\n******** PRODUCT DETAILS ********")
        print("Supermarket:", Product.supermarket_name)
        print("Product ID:", self.__product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Manufacturer:", self.manufacturer)
        print("Weight:", self.weight)
        print("Expiration Date:", self.expiration_date)
        print("Year:", self.year)
        print("*********************************\n")


class Healthy(Product):

    def __init__(self, product_id, name, price, manufacturer, weight, expiration_date, year, components):
        super().__init__(product_id, name, price, manufacturer, weight, expiration_date, year)
        self.calories = 0
        self.components = components

    def change_calories(self):
        self.calories += 1
        print("Calories increased by 1 gram.")
        print("Current Calories:", self.calories, "\n")

    def check_data(self):
        print("\n******** HEALTHY DATA ********")
        print("Calories:", self.calories)
        print("Components:", self.components)
        print("******************************\n")

    def total_calories(self):
        weight = float(input("Enter weight in gram: "))
        total = self.calories * weight
        print("Total Calories =", total, "\n")


print("****************************************")
print("     WELCOME TO SEOUDI SUPERMARKET     ")
print("****************************************\n")

while True:

    print("""
******** MAIN MENU ********
1- Product Sub-System
2- Healthy Sub-System
3- Exit System
***************************
""")

    main_choice = input("Choose: ")

    # ---------------- PRODUCT SYSTEM ----------------
    if main_choice == "1":

        product = None

        print("\n******** PRODUCT SUB-SYSTEM ********")

        while True:

            print("""
1- Add New Product
2- Display Product Details
3- Edit Product ID
4- Exit Sub-System
5- Exit Supermarket System
""")

            choice = input("Choose: ")

            if choice == "1":
                pid = input("Enter Product ID: ")
                name = input("Enter Name: ")
                price = float(input("Enter Price: "))
                manufacturer = input("Enter Manufacturer: ")
                weight = float(input("Enter Weight (gram): "))
                exp = input("Enter Expiration Date: ")
                year = input("Enter Year: ")

                product = Product(pid, name, price, manufacturer, weight, exp, year)
                print("Product added successfully.\n")

            elif choice == "2":
                if product:
                    product.product_detail()
                else:
                    print("No product found.\n")

            elif choice == "3":
                if product:
                    new_id = input("Enter New Product ID: ")
                    product.set_product_id(new_id)
                else:
                    print("No product found.\n")

            elif choice == "4":
                print("Exiting Product Sub-System...\n")
                break

            elif choice == "5":
                print("System Closed. Thank you!")
                sys.exit()

            else:
                print("Invalid choice.\n")

    # ---------------- HEALTHY SYSTEM ----------------
    elif main_choice == "2":

        healthy = None

        print("\n******** HEALTHY SUB-SYSTEM ********")

        while True:

            print("""
1- Add New Healthy Product
2- Display Healthy Details
3- Change Calories (+1 gram)
4- Check Calories & Components
5- Compute Total Calories
6- Exit Sub-System
7- Exit Supermarket System
""")

            choice = input("Choose: ")

            if choice == "1":
                pid = input("Enter Product ID: ")
                name = input("Enter Name: ")
                price = float(input("Enter Price: "))
                manufacturer = input("Enter Manufacturer: ")
                weight = float(input("Enter Weight (gram): "))
                exp = input("Enter Expiration Date: ")
                year = input("Enter Year: ")
                comp = input("Enter Components: ")

                healthy = Healthy(pid, name, price, manufacturer, weight, exp, year, comp)
                print("Healthy product added successfully.\n")

            elif choice == "2":
                if healthy:
                    healthy.product_detail()
                else:
                    print("No healthy product found.\n")

            elif choice == "3":
                if healthy:
                    healthy.change_calories()
                else:
                    print("No healthy product found.\n")

            elif choice == "4":
                if healthy:
                    healthy.check_data()
                else:
                    print("No healthy product found.\n")

            elif choice == "5":
                if healthy:
                    healthy.total_calories()
                else:
                    print("No healthy product found.\n")

            elif choice == "6":
                print("Exiting Healthy Sub-System...\n")
                break

            elif choice == "7":
                print("System Closed. Thank you!")
                sys.exit()

            else:
                print("Invalid choice.\n")

    elif main_choice == "3":
        print("System Closed. Goodbye!")
        break

    else:
        print("Invalid choice.\n")