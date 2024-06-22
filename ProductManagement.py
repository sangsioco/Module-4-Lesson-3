from product_categories import Product, Book, Electronics, Clothing

def add_product(categories):
    while True:
        category = input("Enter product category (Book/Electronics/Clothing): ").lower()

        if category not in ['book', 'electronics', 'clothing']:
            print("Invalid category. Please enter Book, Electronics, or Clothing.")
            continue

        if category == 'book':
            while True:
                product_id = input("Enter product ID: ")
                if product_id in categories.get(category, {}):
                    print(f"Product ID '{product_id}' already exists in '{category}' category. Please enter a different product ID.")
                else:
                    break  # Exit the loop if product_id is unique

            while True:
                title = input("Enter book title: ")
                if any(product.get_title() == title for product in categories.get(category, {}).values()):
                    print(f"Book title '{title}' already exists in '{category}' category. Please enter a different title.")
                else:
                    break  # Exit the loop if title is unique

            author = input("Enter author: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Book(product_id, title, author, price, quantity)
            print("Book added.")

        elif category == 'electronics':
            while True:
                product_id = input("Enter product ID: ")
                if product_id in categories.get(category, {}):
                    print(f"Product ID '{product_id}' already exists in '{category}' category. Please enter a different product ID.")
                else:
                    break  # Exit the loop if product_id is unique

            name = input("Enter product name: ")
            specs = input("Enter specs: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Electronics(product_id, name, specs, price, quantity)
            print("Electronics product added.")

        elif category == 'clothing':
            while True:
                product_id = input("Enter product ID: ")
                if product_id in categories.get(category, {}):
                    print(f"Product ID '{product_id}' already exists in '{category}' category. Please enter a different product ID.")
                else:
                    break  # Exit the loop if product_id is unique

            name = input("Enter product name: ")
            size = input("Enter size: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Clothing(product_id, name, size, price, quantity)
            print("Clothing product added.")

        if category not in categories:
            categories[category] = {}

        categories[category][product_id] = product

        if input("Do you want to add another product? (yes/no): ").lower() != 'yes':
            break

def update_stock(categories):
    category = input("Enter product category (Book/Electronics/Clothing): ")
    if category in categories:
        product_id = input("Enter product ID to update: ")
        if product_id in categories[category]:
            new_quantity = int(input("Enter new quantity: "))
            categories[category][product_id].set_quantity(new_quantity)
        else:
            print("Product not found in this category")
    else:
        print("Category not found")


def process_sale(categories):
    category = input("Enter product category (Book/Electronics/Clothing): ")
    if category in categories:
        product_id = input("Enter product ID for sale: ")
        if product_id in categories[category]:
            quantity_sold = int(input("Enter quantity sold: "))
            product = categories[category][product_id]
            try:
                product.sell(quantity_sold)
                total_price = quantity_sold * product.get_price()
                print(f"Receipt: Sold {quantity_sold} of {product.get_name()} for ${total_price:.2f}")
            except ValueError as e:
                print(e)
        else:
            print("Product not found in this category")
    else:
        print("Category not found")


def display_inventory(categories):
    if categories:
        for category, products in categories.items():
            print(f"Category: {category}")
            total_sold = 0
            for product in products.values():
                product.display()
                total_sold += product.get_sold_quantity()
                print("-" * 20)
    else:
        print("Inventory is empty")


def main():
    categories = {}
    while True:
        print("\nE-Commerce Product Management System\n1. Add Product\n2. Update Stock\n3. Process Sale\n4. Display Inventory\n5. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_product(categories)
            elif choice == '2':
                update_stock(categories)
            elif choice == '3':
                process_sale(categories)
            elif choice == '4':
                display_inventory(categories)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
