from manage_customer import addCustomer, editCustomer, deleteCustomer
from manage_menu import addMenuItem, editMenuItem, deleteMenuItem

def manager_menu():
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
        print("View ingredients list requested by chef")
    elif choice == "4":
        updateProfile()
    elif choice == "5":
        print("Logging out...")
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
        print("4. Back to Admin Menu")

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

def updateProfile():
    print("\n==== Update Manager Profile ====")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        with open("Files/users.txt", "r") as file:
            managers = file.readlines()

        updated_managers = []
        manager_found = False

        for manager in managers:
            data = manager.strip().split(",")
            if len(data) != 3:
                continue
            stored_username, stored_password, role = data

            if stored_username == username and role.lower() == "manager" and stored_password == password:
                manager_found = True
                print("1. Update Username")
                print("2. Update Password")
                choice = input("Enter choice: (1 or 2): ").strip()

                if choice == "1":
                    new_username = input("Enter new username: ").strip()
                    updated_manager = f"{new_username},{password},{role}\n"
                    updated_managers.append(updated_manager)
                    print("Username updated successfully.")
                elif choice == "2":
                    new_password = input("Enter new password: ").strip()
                    updated_manager = f"{stored_username},{new_password},{role}\n"
                    updated_managers.append(updated_manager)
                    print("Password updated successfully.")
                else:
                    print("Invalid choice. Please try again.")
                    return
                
            else:
                updated_managers.append(manager)
        
        if not manager_found:
            print("Manager not found.")
            return
        
        with open("Files/users.txt", "w") as file:
            file.writelines(updated_managers)

    except FileNotFoundError:
        print("No managers found.")

