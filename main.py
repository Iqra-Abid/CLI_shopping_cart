# Defining all the functions
def account():
    # asks the users to create  an account or login,if the account is already created Returns a message indicating the result of the account
    global username
    # using global so that a particular username can be used throughout the program
    i = 0
    j = 0
    x = input(
        "'Create account or 'login'\n press '1' to create an account and '2' to login to your existing account: ")  # asking the user to login or create account
    with open('user_accounts.txt', 'a+') as f:
        f.seek(0)
        lines = f.readlines()  # reads the file 'datas' line by line.

    while j <= 0:
        if x == '1':  # creating account if the user is new.
            firstname = input('Enter your first name:')
            lastname = input('Enter your last name:')
            username = input('Enter your username:')
            password = input('Enter your password:')
            address = input('Enter your address:')
            # create dictionary
            user_info = {
                'username': username,
                'first_name': firstname,
                'last_name': lastname,
                'password': password,
                'address': address
            }
            if any(username in line for line in lines):
                print('Username already exists, restart')
                account()
            else:
                with open('user_accounts.txt', 'a+') as file:
                    file.write(str(user_info) + '\n')  # writes data in the file when user info is given.
                    print('Account creation successful')
                    j = j + 1

        elif x == '2':
            while i < 1:
                username = input('Enter your username:')
                password = input('Enter your password:')
                if any(username in line and password in line for line in
                       lines):  # checking if the username exists or not.
                    print('You are successfully logged into your account')
                    i = i + 1
                    j = j + 1
                else:
                    print('Invalid username or password, please try again')

        else:
            print("Invalid choice")
            x = input(
                "'Create account or 'login'\n press '1' to create an account and '2' to login to your existing account: ")


# Product list
products = [
    {"name": "Hoodie",
     "Price": 3000,
     "description": "cotton"},
    {"name": "Denim Jeans",
     "Price": 3500,
     "description": "navy blue color"},
    {"name": "Denim Jacket",
     "Price": 3700,
     "description": "rare black colour"},
    {"name": "Basic tee",
     "Price": 1700,
     "description": "Round Neck Collar Quarter Sleeves"},
    {"name": "Sweatshirt",
     "Price": 2000,
     "description": "stretch fabric"},
    {"name": "Muffler",
     "Price": 1000,
     "description": "hand knitted"},
    {"name": "Tote Bag",
     "Price": 1500,
     "description": "Leather"},
    {"name": "Body mist",
     "Price": 1400,
     "description": "lavender"},
    {"name": "Beanie",
     "Price": 1500,
     "description": "cotton"},
    {"name": "Watch",
     "Price": 1000,
     "description": "Stainless steel"},
]

# Save product list in a seperate txt file
with open('product_list.txt', 'w') as file:
    for i in products:
        file.write(str(i) + '\n')

# Initializing the cart as an empty list
cart = []
# Function to display product list to user
def display_product_list():
    print("Product List:")
    for index in range(len(products)):
        product = products[index]
        print(f"{index + 1}. {product['name']}: Rs{product['Price']}")
        print(f"Description:{product['description']}\n")

# Function to add products to cart
def add_to_cart(product_index):
        product = products[product_index - 1]
        quantity = int(input(f"How many {product['name']} would you like to add to your cart? "))
        product['quantity'] = quantity
        cart.append(product)
        print(f"\n{product['name']} (Quantity: {quantity}) has been added to your cart.")

# Function to remove products from the cart
def remove_from_cart(product_index):
    product = cart.pop(product_index - 1)
    print(f"{product['name']} has been removed from your cart.")


# Functions to view items in cart
def view_cart(quantity=None):
    print("YOUR CART:")
    for product in cart:
        print(f"Name: {product['name']}")
        print(f"Price: {product['Price']}")
        print(f"Description: {product['description']}")
        print(f"Quantity:{product['quantity']}")
        print()


# function to save and view shopping history
import datetime


def view_shopping_history():
    global username
    # Get the current timestamp
    timestamp = datetime.datetime.now()
    # Extract date time from timestamp
    date = timestamp.strftime('%Y-%m-%d')
    time = timestamp.strftime('%H:%M:%S')
    # Create a file
    checkout_details = f"view_shopping_history.txt"
    # Open the file in write mode
    with open('view_shopping_history.txt', "a") as file:
        # Write the header
        file.write(f"\n\nShopping history & Checkout Details of {username}:\n")
        # write date and time in file
        file.write(f"Date:{date}\n")
        file.write(f"Time:{time}\n")
        file.write("\n")
        # Write each product in the cart
        for product in cart:
            file.write(f"Name:{product['name']}\n")
            file.write(f"Price:{product['Price']}\n")
            file.write(f"Description:{product['description']}\n")
            file.write(f"Quantity:{product['quantity']}\n")
            file.write("\n")

            print("Your shopping history:\n")
            print(f"Date:{date}\n")
            print(f"Time:{time}\n")
            for product in cart:
                print(f"Name: {product['name']}")
                print(f"Price: {product['Price']}")
                print(f"Description: {product['description']}")
                print(f"Quantity:{product['quantity']}")
                print()

# Function to calculate the bill
def calculate_total_price():
    total_price = sum(product['Price'] * product['quantity'] for product in cart)
    print(f"Total Price: Rs{total_price}")
    with open("view_shopping_history.txt", 'a') as file:
        file.write(f"Total Price: Rs{total_price}\n")


# function to save checkout details or cart details
def save_checkout_details():
    # Get the current timestamp
    timestamp = datetime.datetime.now()
    # Extract the date and time from the timestamp
    date = timestamp.strftime('%Y-%m-%d')
    time = timestamp.strftime('%H:%M:%S')
    # Create a file name with the timestamp
    cart_details = f"cart_details.txt"

    # Open the file in write mode
    with open(cart_details, "w") as file:
        # Write the header
        file.write("Cart Details:\n")
        # Write the date and time
        file.write(f"Date: {date}\n")
        file.write(f"Time: {time}\n")
        file.write("\n")
        # Write each product in the cart
        for product in cart:
            file.write(f"Name: {product['name']}\n")
            file.write(f"Price: {product['Price']}\n")
            file.write(f"Description: {product['description']}\n")
            file.write(f"Quantity:{product['quantity']}\n")
            file.write("\n")


# Start of application

print("\n                                 WELCOME TO TRENDTHREAD!!!                           ")
print(
    "Where fashion meets flair!\n\"Explore our curated collection of outfits, tote bags , mists, watches and more to elevate your style game\"")

# Main program flow
print("\nWhat would you like to do?\n")
account()

while True:
    print("\n1. Display Product List")
    print("2. Add Products to Cart")
    print("3. Remove Product from Cart")
    print("4. View Cart")
    print("5. View shopping history")
    print("6. Checkout")
    print("7. Exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_product_list()

    elif choice == "2":
        product_index = int(input("Enter the product number to add to your cart: "))
        if 1 <= product_index <= 10:
            add_to_cart(product_index)
        else:
            print("Please enter a valid product number")

    elif choice == "3":
        if len(cart) == 0:
            print('Your cart is empty')
        else:
            view_cart()
            product_index = int(input("Enter the product number to remove from 'YOUR CART': "))
            if 1 <= product_index <= 10:
                remove_from_cart(product_index)
            else:
                print("Please enter a valid product number from 'YOUR CART'")

    elif choice == "4":
        if len != 0:
            view_cart()
    elif choice == "5":
        view_shopping_history()

    elif choice == "6":
        calculate_total_price()
        save_checkout_details()
    elif choice == "7":
        print("Thank you for shopping. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# **********************************************************************************************************************

# **********************************************************************************************************************
# **********************************************************************************************************************1
