import json

def create_product():
    product = {}
    product['name'] = input("Enter product name: ")
    product['price'] = float(input("Enter product price: "))
    product['created_date'] = input("Enter product creation date (YYYY-MM-DD): ")
    product['current_count'] = int(input("Enter current count: "))
    product['sell_count'] = int(input("Enter sell count: "))
    product['product_id'] = input("Enter product ID: ")
    return product

def save_to_json(product):
    try:
        with open('products.json', 'r+') as file:
            products = json.load(file)
            products.append(product)
            file.seek(0)  # Move to the beginning of the file
            json.dump(products, file, indent=4)
            print("Product added successfully.")
    except FileNotFoundError:
        with open('products.json', 'w') as file:
            json.dump([product], file, indent=4)
            print("Product added successfully.")

def main():
    while True:
        action = input("Do you want to add a new product? (yes/no): ").lower()
        if action == 'yes':
            product = create_product()
            save_to_json(product)
        elif action == 'no':
            break
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
