import json
import os

def load_products_from_json():
    if os.path.exists('products.json'):
        with open('products.json', 'r') as file:
            return json.load(file)
    return []

def find_product_by_id(products, product_id):
    for product in products:
        if product['product_id'] == product_id:
            return product
    return None

def update_product_sell_count_and_current_count(product, increase_sell_count):
    if product is None:
        print("Product not found.")
        return
    if increase_sell_count > 0:
        new_sell_count = product['sell_count'] + increase_sell_count
        new_current_count = max(product['current_count'] - increase_sell_count, 0)
        product['sell_count'] = new_sell_count
        product['current_count'] = new_current_count
        print(f"Updated product: {product}")
        return True
    else:
        print("Increase sell count must be greater than 0.")
        return False

def save_updated_products_to_json(products):
    with open('products.json', 'w') as file:
        json.dump(products, file, indent=4)
    print("Product data updated successfully.")

def main():
    products = load_products_from_json()
    product_id = input("Enter product ID to search: ")
    product = find_product_by_id(products, product_id)
    if product:
        increase_sell_count = int(input("Enter number to increase sell count: "))
        if update_product_sell_count_and_current_count(product, increase_sell_count):
            save_updated_products_to_json(products)
        else:
            print("Failed to update product.")
    else:
        print("No product found with the given ID.")

if __name__ == "__main__":
    main()
