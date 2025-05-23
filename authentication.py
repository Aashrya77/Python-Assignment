from admin_manager_functions.admin_functions import adminMenu
from admin_manager_functions.manager_funtions import manager_menu
from chef_customer_functions.chef import main_program
from chef_customer_functions.customer import customer_program
#User Authentication
def loginUser ():
    MaxAttempts = 3
    while MaxAttempts > 0:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        user_found = False
        correct_password = False
        user_role = None

        with open("Files/users.txt", "r") as file:
            users = file.readlines()

            for user in users:
                if not user.strip():
                    continue
                stored_username, stored_password, role = user.strip().split(",")

                if username.lower() == stored_username.lower():
                    user_found = True
                    if password == stored_password:
                        correct_password = True
                        user_role = role
                    break
            if not user_found:
                print("User not found")
            elif not correct_password:
                print("Incorrect password")
            
            elif user_found and correct_password:
                print(f"Welcome {username.capitalize()}! You are logged in as {user_role}")
                redirectUser(user_role.lower())
                return user_role
            
            MaxAttempts -= 1
            print(f"Login failed! {MaxAttempts} attempts remaining")
    print("You have exceeded the maximum number of attempts. Please try again later.")
    return None

def redirectUser (role):
    if role == "admin":
        adminMenu()
    elif role == "customer":
        customer_program()
    elif role == "manager":
        manager_menu()
    elif role == "chef":
       main_program()
