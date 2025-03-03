import os

# File names for storing data
transactions_file = 'transactions.txt'  # Keeps track of orders
supplies_file = 'supplies.txt'          # List of kitchen items
user_settings_file = 'user_settings.txt' # Stores user preferences

def show_main_menu():
    """Show the main options menu"""
    print("\nMain Menu:")
    print("1. View Order History")
    print("2. Update Order Status")
    print("3. Manage Kitchen Supplies")
    print("4. Change User Settings")
    print("5. Exit Program")

def get_orders():
    """Get all orders from the storage file"""
    if not os.path.exists(transactions_file):
        return []
    with open(transactions_file, 'r') as file:
        return [line.strip().split(',') for line in file]

def save_orders(orders):
    """Save orders back to file"""
    with open(transactions_file, 'w') as file:
        for order in orders:
            file.write(','.join(order) + '\n')

def show_orders():
    """Display all current orders"""
    all_orders = get_orders()
    if not all_orders:
        print("No orders found.")
        return
    for order in all_orders:
        print(f"Order {order[0]}: {order[1]} - Status: {order[2]}")

def update_order():
    """Change an order's status"""
    orders = get_orders()
    order_id = input("Enter order number: ")
    
    # Find the order
    found_order = None
    for order in orders:
        if order[0] == order_id:
            found_order = order
            break
    
    if not found_order:
        print("Order not found.")
        return
    
    new_status = input("New status (Preparing/Ready): ")
    if new_status not in ["Preparing", "Ready"]:
        print("Invalid status.")
        return
    
    found_order[2] = new_status
    save_orders(orders)
    print(f"Order {order_id} updated to {new_status}")

def manage_supplies():
    """Handle kitchen inventory"""
    # Get current supplies
    if not os.path.exists(supplies_file):
        supplies = []
    else:
        with open(supplies_file, 'r') as file:
            supplies = [line.strip() for line in file]
    
    print("\nKitchen Supplies:")
    print("1. Add New Item")
    print("2. Rename Item")
    print("3. Remove Item")
    choice = input("What would you like to do? ")
    
    if choice == '1':
        new_item = input("Enter new supply item: ")
        supplies.append(new_item)
    elif choice == '2':
        old_name = input("Item to rename: ")
        if old_name in supplies:
            new_name = input("New name: ")
            supplies[supplies.index(old_name)] = new_name
        else:
            print("Item not found.")
    elif choice == '3':
        remove_item = input("Item to remove: ")
        if remove_item in supplies:
            supplies.remove(remove_item)
        else:
            print("Item not found.")
    else:
        print("Invalid choice.")
    
    # Save changes
    with open(supplies_file, 'w') as file:
        for item in supplies:
            file.write(item + '\n')

def change_settings():
    """Update user preferences"""
    settings = {}
    if os.path.exists(user_settings_file):
        with open(user_settings_file, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                settings[key] = value
    
    print("\nCurrent Settings:")
    for setting, value in settings.items():
        print(f"{setting}: {value}")
    
    setting_name = input("Which setting to change? ")
    if setting_name not in settings:
        print("Invalid setting.")
        return
    
    new_value = input(f"New value for {setting_name}: ")
    settings[setting_name] = new_value
    
    with open(user_settings_file, 'w') as file:
        for key, value in settings.items():
            file.write(f"{key}={value}\n")
    print("Settings updated.")

def main_program():
    """Main program loop"""
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            show_orders()
        elif choice == '2':
            update_order()
        elif choice == '3':
            manage_supplies()
        elif choice == '4':
            change_settings()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_program()