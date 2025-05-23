import os
from datetime import datetime

# Data files
menu_file = 'Files/menu.txt'            # Food items with prices
orders_file = 'Files/orders.txt'        # Customer orders
feedback_file = 'Files/feedback.txt'    # Customer feedback
profile_file = 'customer_profiles.txt'
chef_profile_file = 'chef_profile.txt'  # Customer profiles

def show_customer_menu():
    """Display customer options"""
    print("\nCustomer Menu:")
    print("1. View Menu & Place Order")
    print("2. Check My Order Status")
    print("3. Leave Feedback")
    print("4. Update My Profile")
    print("5. Exit")

#customer functions
def get_menu_items():
    """Get list of food items"""
    if not os.path.exists(menu_file):
        return []
    with open(menu_file, 'r') as file:
        return [line.strip().split(',') for line in file]
#show menu
def show_menu():
    """Display available food items"""
    print("\nToday's Menu:")
    menu = get_menu_items()
    for num, item in enumerate(menu, 1):
        category, name, price = item[0], item[1], item[2].strip()
        print(f"{num}. {name} - ${price} ({category})")

def place_order():
    """Handle food ordering process"""
    current_order = []
    while True:
        show_menu()
        print("\nOrder Options:")
        print("1. Add Item to Order")
        print("2. Edit Item in Order")
        print("3. Remove Item from Order")
        print("4. Finish Order")
        print("5. Cancel Order")
        
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
                edit_num = int(input("Enter item number to edit: ")) - 1
                selected = current_order[edit_num]
                show_menu()
                new_item_num = int(input("Enter new menu number: ")) - 1
                menu = get_menu_items()
                new_item = menu[new_item_num]
                current_order[edit_num] = new_item
                print(f"Edited {selected[0]} to {new_item[0]}")
            except:
                print("Invalid selection")
        
        elif action == '3':
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
        
        elif action == '4':
            if not current_order:
                print("Please add items first")
                continue
            
            total = sum(float(item[2]) for item in current_order)
            print(f"Total: ${total:.2f}")
            confirm = input("Confirm purchase (yes/no)? ").lower()
            
            if confirm == 'yes':
                save_order(current_order)
                print("Order placed successfully!")
                return
            else:
                print("Order cancelled")
                return
        
        elif action == '5':
            print("Order cancelled")
            return
        
        else:
            print("Invalid choice")

def save_order(items):
    """Save order to file"""
    with open(orders_file, 'a') as file:
        order_id = str(len(open(orders_file).readlines()) + 1)
        food_items = ';'.join([f"{item[1]}${item[2]}" for item in items])
        order_date = datetime.now().strftime("%Y-%m-%d")
        file.write(f"{order_id},{order_date},{food_items},In Progress\n")
        print("Order saved")

def check_order():
    """Check status of an order"""
    order_id = input("Enter your order number: ")
    with open(orders_file, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == order_id:
                print(f"\nOrder Status: {parts[3]}")
                print("Items Ordered:")
                for item in parts[2].split(';'):
                    name, price = item.split('$')
                    print(f"- {name} (${price})")
                return
    print("Order not found")


def leave_feedback():
    """Save customer feedback with auto-filled customer and chef names"""
    customer_name = input("Enter your name: ")
    chef_name = input("Enter the name of chef you want to give feedback to: ")
    feedback_text = input("How was your experience? (max 200 characters)\n")
    chef_found = False
    if len(feedback_text) > 200:
        print("Please keep feedback under 200 characters")
        return
    current_date = datetime.today().strftime('%Y-%m-%d')
    feedback_entry = f"{current_date},{customer_name},Chef {chef_name},{feedback_text}\n"

    with open(feedback_file, 'a') as file:
        file.write(feedback_entry)
    
    print("Thank you for your feedback!")

def update_profile ():
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
                print("1. Username or passoword")
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

                    if role == "Customer":
                        profile_found = False                    
                        try: 
                            with open("Files/customer_profiles.txt", "r") as file:
                                profiles = file.readlines()

                            for j, line in enumerate(profiles):
                                data = line.strip().split(",")
                                if data[0].lower() == current_username.lower():
                                    profile_found = True
                                    data[0] = new_username
                                    profiles[j] = ",".join(data) + '\n'
                                    break
                            print(profile_found)
                            if profile_found:
                                with open("Files/customer_profiles.txt", "w") as file:
                                    file.writelines(profiles)
                        except FileNotFoundError:
                            print("No profile found")
                
                elif choice == "2":
                    profile_found = False
                    try:
                        with open("Files/customers.txt", "r") as file:
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
                            with open("Files/customers.txt", "w") as file:
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
