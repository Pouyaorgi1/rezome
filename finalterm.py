import os

def save_data(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(data))
    except IOError as e:
        print(f"Error saving data: {e}")

def load_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                return [line.strip() for line in file]
        except IOError as e:
            print(f"Error loading data: {e}")
    return []

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Manager(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.customers = {}
        self.products = {}
        self.categories = {"Clothings": [145], "Groceries": [34]}
        self.load_products()

    def load_products(self):
        self.products[145] = {"name": "jeans", "price": 77, "category": "Clothings"}
        self.products[34] = {"name": "apple", "price": 20, "category": "Groceries"}

    def add_category(self, category):
        if category not in self.categories:
            self.categories[category] = []
            print(f"Category '{category}' added successfully.")
        else:
            print(f"Category '{category}' already exists.")

    def remove_category(self, category):
        if category in self.categories:
            del self.categories[category]
            print(f"Category '{category}' removed successfully.")
        else:
            print(f"Category '{category}' does not exist.")

    def add_product(self, category, product_name, product_id, price):
        if category in self.categories:
            self.products[product_id] = {"name": product_name, "price": price, "category": category}
            self.categories[category].append(product_id)
            print(f"Product '{product_name}' added successfully.")
        else:
            print(f"Category '{category}' does not exist.")

    def remove_product(self, product_id):
        if product_id in self.products:
            category = self.products[product_id]["category"]
            self.categories[category].remove(product_id)
            del self.products[product_id]
            print(f"Product ID '{product_id}' removed successfully.")
        else:
            print(f"Product ID '{product_id}' does not exist.")

    def view_customers(self):
        for customer in self.customers.values():
            print(f"ID: {customer.username}, Name: {customer.name}, Card Number: {customer.card_number}, Balance: {customer.balance}, Shopping History: {customer.history}")

    def access_customer_account(self, username):
        if username in self.customers:
            return self.customers[username]
        else:
            print("Customer not found.")
            return None

class Customer(User):
    def __init__(self, username, password, name, card_number):
        super().__init__(username, password)
        self.name = name
        self.card_number = card_number
        self.balance = 0
        self.cart = []
        self.history = []

    def add_to_cart(self, product_id, manager):
        if product_id in manager.products:
            self.cart.append(product_id)
            print("Product added to cart.")
        else:
            print("Product ID not found.")

    def view_cart(self, manager):
        total = 0
        for product_id in self.cart:
            product = manager.products.get(product_id)
            if product:
                print(f"{product['name']} - ${product['price']}")
                total += product['price']
        print(f"Total: ${total}")

    def purchase(self, manager):
        total = sum(manager.products[product_id]['price'] for product_id in self.cart)
        if total <= self.balance:
            self.balance -= total
            self.history.extend(self.cart)
            self.cart = []
            print("Purchase successful.")
        else:
            print("pool nadari")

    def top_up(self, amount):
        self.balance += amount
        print(f"Account topped up by ${amount}. New balance: ${self.balance}")

    def view_history(self, manager):
        for product_id in self.history:
            product = manager.products.get(product_id)
            if product:
                print(f"{product['name']} - ${product['price']}")

manager = Manager("pouya", "9940")

while True:
    print("Welcome to the Shopping Store")
    user_type = input("Are you a (1) Manager or (2) moshtari? (Enter 0 to exit): ")

    if user_type == '0':
        break

    if user_type == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == manager.username and password == manager.password:
            print("Welcome, Manager")
            while True:
                print("1. Add Category\n2. Remove Category\n3. Add Product\n4. Remove Product\n5. View Customers\n6. Access Customer Account\n7. Logout")
                choice = input("Enter your choice: ")

                try:
                    if choice == '1':
                        category = input("Enter category name: ")
                        manager.add_category(category)
                    elif choice == '2':
                        category = input("Enter category name: ")
                        manager.remove_category(category)
                    elif choice == '3':
                        category = input("Enter category name: ")
                        product_name = input("Enter product name: ")
                        product_id = int(input("Enter product ID: "))
                        price = float(input("Enter product price: "))
                        manager.add_product(category, product_name, product_id, price)
                    elif choice == '4':
                        product_id = int(input("Enter product ID: "))
                        manager.remove_product(product_id)
                    elif choice == '5':
                        manager.view_customers()
                    elif choice == '6':
                        username = input("Enter customer username: ")
                        customer = manager.access_customer_account(username)
                        if customer:
                            while True:
                                print("Customer Menu:\n1. View Cart\n2. View History\n3. Logout")
                                sub_choice = input("Enter your choice: ")
                                if sub_choice == '1':
                                    customer.view_cart(manager)
                                elif sub_choice == '2':
                                    customer.view_history(manager)
                                elif sub_choice == '3':
                                    break
                                else:
                                    print("Invalid choice.")
                    elif choice == '7':
                        break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input. Please enter valid information.")
        else:
            print("Invalid manager credentials.")

    elif user_type == '2':
        action = input("Do you want to (1) Sign Up, (2) Sign In, or (3) Just Visit? ")

        if action == '1':
            while True:
                try:    
                    username = input("Enter a new username: ")
                    if not username:
                        raise ValueError("username cant be empty")
                    password = input("Enter a new password: ")
                    if not password:
                        raise ValueError("password cant be empty")
                    name = input("Enter your name: ")
                    if not name:
                        raise ValueError("name cant be empty")
                    card_number = input("Enter your card number: ")
                    if not card_number:
                        raise ValueError("card number cant be empty")
                    if username not in manager.customers:
                        manager.customers[username] = Customer(username, password, name, card_number)
                        print("Sign up successful.")
                    else:
                        print("Username already exists.")
                    break
                except ValueError as error:
                    print(f"Invalid {error}")

        elif action == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in manager.customers and manager.customers[username].password == password:
                customer = manager.customers[username]
                print(f"Welcome, {customer.name}")
                while True:
                    print("1. View Products\n2. View Cart\n3. Add to Cart\n4. Purchase\n5. charging \n6. View History\n7. Logout")
                    choice = input("Enter your choice: ")

                    try:
                        if choice == '1':
                            for category, product_ids in manager.categories.items():
                                print(f"Category: {category}")
                                for product_id in product_ids:
                                    product = manager.products[product_id]
                                    print(f"{product_id}: {product['name']} - ${product['price']}")
                        elif choice == '2':
                            customer.view_cart(manager)
                        elif choice == '3':
                            product_id = int(input("Enter product ID to add to cart: "))
                            customer.add_to_cart(product_id, manager)
                        elif choice == '4':
                            customer.purchase(manager)
                        elif choice == '5':
                            amount = float(input("Enter amount to top up: "))
                            customer.top_up(amount)
                        elif choice == '6':
                            customer.view_history(manager)
                        elif choice == '7':
                            break
                        else:
                            print("Invalid choice.")
                    except ValueError:
                        print("Invalid input. Please enter valid information.")
            else:
                print("Invalid customer credentials.")

        elif action == '3':
            while True:
                print("Viewing Products")
                for category, product_ids in manager.categories.items():
                    print(f"Category: {category}")
                    for product_id in product_ids:
                        product = manager.products[product_id]
                        print(f"{product_id}: {product['name']} - ${product['price']}")
                back = input("Enter 'b' to go back: ")
                if back == 'b':
                    break
        else:
            print("Invalid action.")

    else:
        print("Invalid user type.")
