item_name = ""
item_quantity = 0
item_price = 0.0
item_unit = ""

while True:
    print()
    print("==== this is a stockroom ====")
    print("1. Add item")
    print("2. Update item")
    print("3. View inventory")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        while True:
            item_name = input("Enter the item name: ").strip()
            if item_name == "":
                print("Name cannot be empty. Please enter a valid name.")
            else:
                break

        while True:
            try:
                item_quantity = int(input("Enter the item quantity: "))
                if item_quantity < 0:
                    print("Quantity cannot be negative. Please enter a valid quantity.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number for the quantity.")

        while True:
            try:
                item_price = float(input("Enter the item price: "))
                if item_price <= 0:
                    print("Price must be more than 0. Please enter a valid price.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the price.")

        while True:
            item_unit = input("Enter the item unit: ").strip()
            if item_unit == "":
                print("Unit cannot be empty. Please enter a valid unit.")
            else:
                break

        print(f"{item_name} added successfully")

    elif choice == "2":
        if item_name == "":
            print("No items in inventory, add an item first")
        else:
            print(f"Current item name: {item_name}")
        while True:
            new_name = input("Enter the new item name (leave blank to keep current): ").strip()
            if new_name != "":
                item_name = new_name
                break
            else:
                print("Name cannot be empty. Please enter a valid name.")
        while True:
            try:
                new_quantity = input("Enter the new item quantity (leave blank to keep current): ").strip()
                if new_quantity == "":
                    break
                new_quantity = int(new_quantity)
                if new_quantity < 0:
                    print("Quantity cannot be negative. Please enter a valid quantity.")
                else:
                    item_quantity = new_quantity
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number for the quantity.")
        while True:
            try:
                new_price = input("Enter the new item price (leave blank to keep current): ").strip()
                if new_price == "":
                    break
                new_price = float(new_price)
                if new_price <= 0:
                    print("Price must be more than 0. Please enter a valid price.")
                else:
                    item_price = new_price
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the price.")
        while True:
            new_unit = input("Enter the new item unit (leave blank to keep current): ").strip()
            if new_unit != "":
                item_unit = new_unit
                break
            else:
                print("Unit cannot be empty. Please enter a valid unit.")
        print(f"{item_name} updated successfully")
       
    elif choice == "3":
        if item_name == "":
            print("No items in inventory, add an item first")
        else:
            print(f"Item Name: {item_name}")
            print(f"Item Quantity: {item_quantity}")
            print(f"Item Price: ${item_price:.2f}")
            print(f"Item Unit: {item_unit}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice, pick 1-4")