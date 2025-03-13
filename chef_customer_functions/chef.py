import os

# File names for storing data
transactions_file = 'Files/orders.txt'  # Keeps track of orders
supplies_file = 'Files/ingredients.txt'          # List of kitchen items
profile_file = 'chef_profile.txt'       # Chef profile

def show_main_menu():
    """Show the main options menu"""
    print("\nMain Menu:")
    print("1. View Order History")
    print("2. Update Order Status")
    print("3. Request Ingredients")
    print("4. Update Profile")
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
    
    new_status = input("New status (In Progress/Completed): ")
    if new_status not in ["In Progress", "Completed"]:
        print("Invalid status.")
        return
    
    found_order[2] = new_status
    save_orders(orders)
    print(f"Order {order_id} updated to {new_status}")

def manage_supplies():
    """Handle kitchen inventory"""
    if not os.path.exists(supplies_file):
        supplies = []
    else:
        with open(supplies_file, 'r') as file:
            supplies = [line.strip() for line in file]
    
    print("\nKitchen Ingredients:")
    print("1. Add New Item")
    print("2. Edit Item")
    print("3. Remove Item")
    choice = input("What would you like to do? ")
    
    if choice == '1':
        new_item = input("Enter new supply item: ")
        supplies.append(new_item)
    elif choice == '2':
        old_name = input("Item to edit: ")
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

def update_Profile ():
    print("\n==== Update Profile ====")
    current_username = input("Enter current username: ").strip()
    current_password = input("Enter current password: ").strip()
    user_found = False
    try:
        with open("Files/users.txt", "r") as file:
            users = file.readlines()
            
        for i, user in enumerate(users):
            data = user.strip().split(',')
            if len(data) != 3:
                continue
            username, password, role = data
            if username.strip().lower() == current_username.strip().lower() and password.strip() == current_password:
                user_found = True
                print("What would you like to update?")
                print("1. Username or passowrd")
                print("2. Phone number, email, or address")
                
                choice = input("Enter choice (1/2): ").strip()

                if choice == "1":
                    print("1. Update Username")
                    print("2. Update Password")
                    print("3. Update both")
                    choice = input("Enter choice (1/2/3): ").strip()

                    new_username, new_password = username, password
                    if(choice == "1"):
                        new_username = input("Enter new username: ").strip()
                    elif(choice == "2"):
                        new_password = input("Enter new password: ").strip()
                    elif(choice == "3"):
                        new_username = input("Enter new username: ").strip()
                        new_password = input("Enter new password: ").strip()
                    else:
                        print("Invalid choice. Update canceled")
                        return
                    users[i] = f"{new_username},{new_password},{role}\n"

                    if role == "Chef":
                        profile_found = False

                    

                        try: 
                            with open("Files/chef_profile.txt", "r") as file:
                                profiles = file.readlines()

                            for j, line in enumerate(profiles):
                                data = line.strip().split(",")
                                if data[0].lower() == current_username.lower():
                                    profile_found = True
                                    data[0] = new_username
                                    profiles[j] = ",".join(data) + '\n'
                                    break
                                
                            if profile_found:
                                with open("Files/chef_profile.txt", "w") as file:
                                    file.writelines(profiles)
                        except FileNotFoundError:
                            print("No profile found")
                
                elif choice == "2":
                    profile_found = False
                    try:
                        with open("Files/chef_profile.txt", "r") as file:
                            profiles = file.readlines()
                            for j, line in enumerate(profiles):
                                data = line.strip().split(",")
                                if data[0].lower() == current_username.lower():
                                    profile_found = True
                                    print("1. Update Email")
                                    print("2. Update Phone number")
                                    print("3. Update Address")
                                    print("4. Update all")
                                    choice = input("Enter choice (1/2/3/4): ").strip()
                                    if choice == "1":
                                        new_email = input("Enter new email: ").strip()
                                        data[1] = new_email
                                    elif choice == "2":
                                        new_phone = input("Enter new Phone number: ").strip()
                                        data[2] = new_phone
                                    elif choice == "3":
                                        new_address = input("Enter new address: ").strip()
                                        data[3] = new_address
                                    elif choice == "4":
                                        new_email = input("Enter new email: ").strip()
                                        new_phone = input("Enter new phone number: ").strip()
                                        
                                        new_address = input("Enter new address: ").strip()
                                        data[1] = new_email
                                        data[2] = new_phone
                                        data[3] = new_address
                                    else:
                                        print("Invalid choice. Update canceled")
                                        return
                                    profiles[j] = ",".join(data) + '\n'
                                    break
                        if profile_found:
                            with open("Files/chef_profile.txt", "w") as file:
                                file.writelines(profiles)
                        else:
                            print("Profile not found")
                    except FileNotFoundError:
                        print("Chef profile not found.")
        

           
                    
                
               
        if user_found:
            with open("Files/users.txt", "w") as file:
                file.writelines(users)
            print("Profile updated successfully")
            
        else:    
            print("Invalid username or password. Update failed")
    except FileNotFoundError:
        print("No user found")




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
            update_Profile()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

