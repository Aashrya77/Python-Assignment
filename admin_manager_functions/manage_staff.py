def viewAllStaff():
    print("\n==== View All Staff ====")
    try:
        with open("Files/users.txt", "r") as file:
            staff = file.readlines()
            if not staff:
                print("No record found")
            else:
                print("Name | Role")
                print("----------------------------")
                for staff_member in staff:
                    role = staff_member.strip().split(",")[-1]
                    username = staff_member.strip().split(",")[0]
                    if role == 'Manager' or role == 'Chef' :
                        print(f"{username} | {role}")
                    
    except FileNotFoundError:
        print("No staff record found")

def addStaff ():
    print("\n==== Add Staff ====")
    username = input("Enter username for new staff member: ").strip()
    password = input("Enter password: ")
    role = input("Enter role (Manager, chef): ").lower().capitalize()

    if role not in ["Manager", "Chef"]:
        print("Invaid role. Only 'Manager' and 'Chef' are allowed.")
        return 
    
    with open('Files/users.txt', 'r') as file:
        staff = file.readlines()
        for staff_member in staff:
            if username == staff_member.strip().split(",")[0]:

                print("Username already exists")
                return
    
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()
    address = input("Enter address: ").strip()
   
    with open("Files/users.txt", "a") as file:
        file.write(f"\n{username},{password},{role}")
    print("Staff added successfully")

    profile_file = "Files/chef_profile.txt" if role == "Chef" else "Files/managers.txt"
    with open(profile_file, 'a') as file:
        file.write(f"\n{username},{email},{phone},{address}")

    print(f"{role} added successfully!")

def updateStaff ():
    print("\n==== Update Staff ====")
    username = input("Enter the username of the staff you want to edit: ")
    user_found = False
    try:
        with open('Files/users.txt', 'r') as file:
            staff = file.readlines()
        for i, staff_member in enumerate(staff):
            data= staff_member.strip().split(",")

            if len(data) != 3:
                continue
            stored_username, password, role = data
            if username == stored_username:
                user_found = True
                new_role = input(f"Enter new role for {username} (Manager, Chef): ").strip()
                if new_role in ["Manager", "Chef"]:
                    staff[i] = f"{username},{password},{new_role}\n"
                    print(f"Role of {username} updated to {new_role}")
                else: 
                    print("Invalid role input")
                    return
                break
        if user_found:
            with open("Files/users.txt", 'w') as file:
                file.writelines(staff)
            print(f"Staff member {username} updated successfully")
        else: 
            print("User Not found")
                    
    except FileNotFoundError:
         print("No staff record found")

def removeStaff ():
    print("\n==== Remove Staff ====")
    username = input("Enter the username of the staff you want to remove: ")
    user_found = False

    try: 
        with open('Files/users.txt', 'r') as file:
            staff = file.readlines()
    except FileNotFoundError:
        print("No staff record found")
        return
    for i, staff_member in enumerate(staff):
        stored_username, password, role = staff_member.strip().split(",")
        if username == stored_username:
            user_found = True
            staff.pop(i)
            break
    if user_found:
        with open("Files/users.txt", 'w') as file:
            file.writelines(staff)
        print(f"Staff member {username} removed successfully")
    else:
        print("User not found")
