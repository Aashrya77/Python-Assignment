import os

# Data files
menu_file = 'menu.txt'           # Food items with prices
orders_file = 'orders.txt'       # Customer orders
feedback_file = 'feedback.txt'   # Customer comments
profile_file = 'profiles.txt'    # User information

def show_customer_menu():
    """Display customer options"""
    print("\nCustomer Menu:")
    print("1. View Menu & Place Order")
    print("2. Check My Order Status")
    print("3. Leave Feedback")
    print("4. Update My Profile")
    print("5. Exit")

def get_menu_items():
    """Get list of food items"""
    if not os.path.exists(menu_file):
        return []
    with open(menu_file, 'r') as file:
        return [line.strip().split(',') for line in file]

def show_menu():
    """Display available food items"""
    print("\nToday's Menu:")
    menu = get_menu_items()
    for num, item in enumerate(menu, 1):
        print(f"{num}. {item[0]} - ${item[1]} ({item[2]})")

def place_order():
    """Handle food ordering process"""
    current_order = []
    while True:
        show_menu()
        print("\nOrder Options:")
        print("1. Add Item to Order")
        print("2. Remove Item from Order")
        print("3. Finish Order")
        print("4. Cancel Order")
        
        action = input("What would you like to do? ")
        
        if action == '1':
            try:
                item_num = int(input("Enter menu number: ")) - 1
                menu = get_menu_items()
                selected = menu[item_num]
                current_order.append(selected)
                print(f"Added {selected[0]}")
            except:
                print("Invalid selection")
        
        elif action == '2':
            if not current_order:
                print("Your order is empty")
                continue
            print("Your Order:")
            for num, item in enumerate(current_order, 1):
                print(f"{num}. {item[0]}")
            try:
                remove_num = int(input("Enter item to remove: ")) - 1
                removed = current_order.pop(remove_num)
                print(f"Removed {removed[0]}")
            except:
                print("Invalid selection")
        
        elif action == '3':
            if not current_order:
                print("Please add items first")
                continue
            
            total = sum(float(item[1]) for item in current_order)
            print(f"Total: ${total:.2f}")
            confirm = input("Confirm purchase (yes/no)? ").lower()
            
            if confirm == 'yes':
                save_order(current_order)
                print("Order placed successfully!")
                return
            else:
                print("Order cancelled")
                return
        
        elif action == '4':
            print("Order cancelled")
            return
        
        else:
            print("Invalid choice")

def save_order(items):
    """Save order to file"""
    with open(orders_file, 'a') as file:
        order_id = str(len(open(orders_file).readlines()) + 1)
        food_items = ';'.join([f"{item[0]}${item[1]}" for item in items])
        file.write(f"{order_id},{food_items},Preparing\n")

def check_order():
    """Check status of an order"""
    order_id = input("Enter your order number: ")
    with open(orders_file, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == order_id:
                print(f"\nOrder Status: {parts[2]}")
                print("Items Ordered:")
                for item in parts[1].split(';'):
                    name, price = item.split('$')
                    print(f"- {name} (${price})")
                return
    print("Order not found")

def leave_feedback():
    """Save customer comments"""
    comment = input("How was your experience? (max 200 characters)\n")
    if len(comment) > 200:
        print("Please keep feedback under 200 characters")
        return
    with open(feedback_file, 'a') as file:
        file.write(comment + "\n")
    print("Thank you for your feedback!")

def update_profile():
    """Update customer information"""
    profile = {}
    if os.path.exists(profile_file):
        with open(profile_file, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                profile[key] = value
    
    print("\nYour Profile:")
    for field, value in profile.items():
        print(f"{field}: {value}")
    
    field = input("What to update? (Name/Email/Phone): ").capitalize()
    new_value = input(f"New {field}: ")
    profile[field] = new_value
    
    with open(profile_file, 'w') as file:
        for key, value in profile.items():
            file.write(f"{key}={value}\n")
    print("Profile updated")

def customer_program():
    """Main customer interface"""
    while True:
        show_customer_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            place_order()
        elif choice == '2':
            check_order()
        elif choice == '3':
            leave_feedback()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    customer_program()