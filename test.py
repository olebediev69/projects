print("Welcome to Shop Database!")
print("""
    Choose action:
        1. Add product (add)
        2. Delete product (delete)
        3. Update price (update)
        4. Show available products (show)
        5. Buy product (buy)
        6. Exit (exit)
""")

database = {}

while True:
    action = input("Enter your choice: ").strip()
    # strip() у Python видаляє всі провідні та завершальні пробіли з рядка.

    if action == "exit" or action == "6":
        print("Thank you for using Shop Database!")
        break

    elif action == "add" or action == "1":
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        while not price.isdigit():
            price = input("Enter a valid price: ")
        quantity = input("Enter product quantity: ")
        while not quantity.isdigit():
            quantity = input("Enter a valid quantity: ")
        database[name] = [int(price), int(quantity)]
        print("Product added to database.")

    elif action == "delete" or action == "2":
        if not database:
            print("No products available to delete.")
        else:
            print("Available products:", list(database.keys()))
            name = input("Enter product name to delete: ")
            while name not in database:
                name = input("Product not found. Enter product name to delete: ")
            del database[name]
            print("Product deleted from database.")

    elif action == "update" or action == "3":
        if not database: #Умова if not database: перевіряє, чи є словник database порожнім. У Python порожній словник оцінюється як False, тоді як непорожній словник оцінюється як True. Таким чином, if not database: виконає блок коду, який слідує за ним, якщо database порожній.

            print("No products available to update.")
        else:
            print("Available products:", list(database.keys()))
            name = input("Enter product name to update: ")
            while name not in database:
                name = input("Product not found. Enter product name to update: ")
            price = input("Enter new product price: ")
            while not price.isdigit():
                price = input("Enter a valid price: ")
            database[name][0] = int(price)
            print("Product price updated.")

    elif action == "show" or action == "4":
        if not database:
            print("No products available.")
        else:
            for name, details in database.items():
                print(f"Product: {name}, Price: {details[0]}, Quantity: {details[1]}")

    elif action == "buy" or action == "5":
        if not database:
            print("No products available to buy.")
        else:
            print("Available products:", list(database.keys()))
            name = input("Enter product name to buy: ")
            while name not in database:
                name = input("Product not found. Enter product name to buy: ")
            quantity = input("Enter quantity to buy: ")
            while not quantity.isdigit():
                quantity = input("Enter a valid quantity: ")
            quantity = int(quantity)
            if quantity <= database[name][1]:
                database[name][1] -= quantity
                print("Product purchased.")
            else:
                print(f"Insufficient quantity available. Available quantity: {database[name][1]}")

    else:
        print("Invalid choice. Please try again.")