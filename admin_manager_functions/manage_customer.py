
def addCustomer():
    print("Add Customer")
    # Add customer code here
    username = input("Enter username: ").strip()
    
    password = input("Enter password: ").strip()
    role = 'Customer'
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()
    address = input("Enter address: ").strip()

    try:
        with open("Files/customers.txt", "r") as file:
            users = file.readlines()
            for user in users:
                if username == user.strip().split(",")[0]:
                    print("Username already exists")
                    return
    except FileNotFoundError:
        pass

    with open("Files/users.txt", "a") as file:
        file.write(f"\n{username},{password},{role}")

    with open("Files/customers.txt", "a") as file:
        file.write(f"\n{username},{email},{phone},{address}")
    
    print("Customer added successfully")
        

def editCustomer():
    print("\n==== Edit Customer ====")
    # Edit customer code here
    username = input("Enter the username of the customer to edit: ").strip()
    customer_found = False

    try:
        with open("Files/customers.txt", "r") as file:
            customers = file.readlines()
            for i, customer in enumerate(customers):
                data = customer.strip().split(",")
                if data[0] == username:
                    customer_found = True
                    current_email, current_phone, current_address = data[1], data[2], data[3]
                    print(f"Current Details: Email={data[1]}, Phone={data[2]}, Address={data[3]}")
                    new_email = input("Enter new email (leave blank to keep current): ").strip() or current_email
                    new_phone = input("Enter new phone (leave blank to keep current): ").strip() or current_phone
                    new_address = input("Enter new address: ").strip() or current_address
                    customers[i] = f"{username},{new_email},{new_phone},{new_address}\n"
                    break

            if customer_found:
                with open("Files/customers.txt", "w") as file:
                    file.writelines(customers)
                print("Customer updated successfully")
            else:
                print("Customer not found")
    except FileNotFoundError:
        print("No customers found")

#delete customer

def deleteCustomer():
    print("\n==== Delete Customer ====")
    # Delete customer code here
    username = input("Enter the username of the customer to delete: ").strip()
    customer_found = False

    try:
        with open("Files/customers.txt", "r") as file:
            customers = file.readlines()
            
            new_customers = [customer for customer in customers if not customer.startswith(username + ",")]
            if len(new_customers) < len(customers):
                customer_found = True
                with open("Files/customers.txt", "w") as file:
                    file.writelines(new_customers)
    except FileNotFoundError:
        print("No customers found")
        return

    if customer_found:
        try:
            with open ("Files/users.txt", "r") as file:
                users = file.readlines()
                new_users = [user for user in users if not user.startswith(username + ",")]
                with open("Files/users.txt", "w") as file:
                    file.writelines(new_users)
                
                print(f"Customer {username} deleted successfully")
        except FileNotFoundError:
            print("No users found")
    else:
        print("Customer not found")

