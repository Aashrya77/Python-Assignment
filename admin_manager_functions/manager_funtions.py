from admin_manager_functions.manage_customer import addCustomer, editCustomer, deleteCustomer
from admin_manager_functions.manage_menu import addMenuItem, editMenuItem, deleteMenuItem

def manager_menu():
    while True: 
        print("\n==== Manager Menu ====")
        print("1. Manage Customer (Add, Edit, Delete)")
        print("2. Manage Menu categories and pricing (Add, Edit, Delete)")
        print("3. View ingredients list requested by chef")
        print("4. Update own profile")
        print("5. Logout")
        
        choice = input("Enter choice: ").strip()
        if choice == "1":
            manageCustomer()
        elif choice == "2":
            manageMenu()
        elif choice == "3":
            viewIngredients()
        elif choice == "4":
            updateProfile()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
            manager_menu()
    

def manageCustomer():
    while True:
        print("\n==== Manager Menu ====")
        print("1. Add New Customer")
        print("2. Update Customer")
        print("3. Remove Customer")
        print("4. Back to Admin Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            addCustomer()
        elif choice == "2":
            editCustomer()
        elif choice == "3":
            deleteCustomer()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again")

def manageMenu():
    while True:
        print("\n==== Manager Menu ====")
        print("1. Add New Menu Item")
        print("2. Update Menu Item")
        print("3. Remove Menu Item")
        print("4. Back to Manager Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            addMenuItem()
        elif choice == "2":
            editMenuItem()
        elif choice == "3":
            deleteMenuItem()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again")

def viewIngredients():
    print("\n==== Ingredients List ====")

    try: 
        with open("Files/ingredients.txt", "r") as file:
            ingredients = file.readlines()

        if not ingredients:
            print("No ingredients requested by chef.")
            return
        
        print("Ingredients requested by chef:")
        for ingredient in ingredients:
            print(ingredient.strip())
    except FileNotFoundError:
        print("No ingredients requested by chef.")

def updateProfile ():
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
                            with open("Files/managers.txt", "r") as file:
                                profiles = file.readlines()

                            for j, line in enumerate(profiles):
                                data = line.strip().split(",")
                                if data[0].lower() == current_username.lower():
                                    profile_found = True
                                    data[0] = new_username
                                    profiles[j] = ",".join(data) + '\n'
                                    break
                                
                            if profile_found:
                                with open("Files/managers.txt", "w") as file:
                                    file.writelines(profiles)
                        except FileNotFoundError:
                            print("No profile found")
                
                elif choice == "2":
                    profile_found = False
                    try:
                        with open("Files/managers.txt", "r") as file:
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
                            with open("Files/managers.txt", "w") as file:
                                file.writelines(profiles)
                        else:
                            print("Profile not found")
                    except FileNotFoundError:
                        print("Manager profile not found.")
        

           
                    
                
               
        if user_found:
            with open("Files/users.txt", "w") as file:
                file.writelines(users)
            print("Profile updated successfully")
            
        else:    
            print("Invalid username or password. Update failed")
    except FileNotFoundError:
        print("No user found")

