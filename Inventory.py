# Inventory Management System

inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}

def display_inventory():
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, quantity in inventory.items():
            print(f"{item}: {quantity} units")

def add_item():
    item = input("Enter item name to add: ").capitalize()
    if item in inventory:
        print("Item already exists. Use 'Update stock' instead.")
    else:
        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            inventory[item] = quantity
            print(f"{item} added with {quantity} units.")
        except ValueError:
            print("Invalid quantity. Must be a number.")

def update_stock():
    item = input("Enter item name to update: ").capitalize()
    if item in inventory:
        try:
            quantity = int(input(f"Enter new quantity for {item}: "))
            inventory[item] = quantity
            print(f"{item} updated to {quantity} units.")
        except ValueError:
            print("Invalid quantity. Must be a number.")
    else:
        print(f"{item} not found in inventory.")

def remove_item():
    item = input("Enter item name to remove: ").capitalize()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed from inventory.")
    else:
        print(f"{item} not found in inventory.")

# Main loop
while True:
    print("\n--- Inventory Management ---")
    print("1. Display Inventory")
    print("2. Add Item")
    print("3. Update Stock")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        update_stock()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        print("Exiting inventory system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        

