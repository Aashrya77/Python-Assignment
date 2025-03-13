from admin_manager_functions.manage_staff import addStaff, updateStaff, removeStaff, viewAllStaff

def adminMenu ():
   while True:
       print("\n==== Admin Menu ====")
       print("1. Manage Staff")
       print("2. View Sales Report")
       print("3. View Feedback")
       print("4. Update Profile")
       print("5. Logout")

       choice = input("Enter choice: ").strip()

       if choice == "1":
            manageStaff()
       elif choice == "2":
            viewSalesReport()
       elif choice == "3":
            viewFeedback()
       elif choice == "4":
            updateProfile()
       elif choice == "5":
            print("Logging out...")
            break
       else:
            print("Invalid choice. Please try again")

def manageStaff ():
    while True:
        print("\n==== Manage Staff ====")
        print("1. View all Staffs")
        print("2. Add New Staff")
        print("3. Update Staff")
        print("4. Remove Staff")
        print("5. Back to Admin Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            viewAllStaff()
        elif choice == "2":
            addStaff()
        elif choice == "3":
            updateStaff()
        elif choice == "4":
            removeStaff()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again")

def viewSalesReport ():
    print("\n==== View Sales Report ====")

    filter_option = input("View report by:\n1. Month\n2. Chef\n3. Overall\n. Choose(1/2/3): ").strip().lower()

    month_filter = None
    chef_filter = None

    if filter_option == '1':
        month_filter = input("Enter month (MM, e.g., 02 for February): ").strip()
    elif filter_option == '2':
        chef_filter = input("Enter chef's name: ").strip().capitalize()
    try:
        with open("Files/sales.txt", "r") as file:
            sales = file.readlines()

            if not sales:
                print("No sales record found")
                return
            
            total_orders = 0
            total_revenue = 0
            item_sales = {}

            for sale in sales:
                if "OrderId" in sale: 
                    continue
                order_id, item, quantity, price, total_price, date, chef = sale.strip().split(",")
                quantity, price, total_price = int(quantity), float(price), float(total_price)
                order_month = date.split("-")[1]

                if month_filter and month_filter != order_month:
                    continue
                if chef_filter and chef_filter != chef:
                    continue

                total_orders += 1
                total_revenue += total_price

                if item not in item_sales:
                    item_sales[item] = {"quantity": quantity, "revenue": total_price}
                else:
                    item_sales[item]["quantity"] += quantity
                    item_sales[item]["revenue"] += total_price
                
            print(f"\nTotal Orders: {total_orders}")
            print(f"Total Revenue: ${total_revenue:.2f}")

            if not total_orders:
                print("No sales record found")
                return
            
            print("\nItem-wise sales summary: ")
            print("Item\t| Quantity\t| Revenue")
            print("-----------------------------------")
            for item, sales in item_sales.items():
                print(f"{item}\t| {sales['quantity']}\t\t| ${sales['revenue']:.2f}")
    except FileNotFoundError:
        print("No sales record found")

def viewFeedback ():
    print("\n==== View Feedback ====")

    try:
        with open("Files/feedback.txt", "r") as file:
            feedbacks = file.readlines()

            if not feedbacks:
                print("No feedback found")
                return
            print("1: View by chef\n2: View feedback by date\n3: View all feedbacks")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                chef_name = input("Enter chef's name: ").strip().capitalize()
                feedbacks = [feedback for feedback in feedbacks if chef_name in feedback]
            elif choice == "2":
                try:
                    date = input("Enter date (YYYY-MM-DD): ").strip()
                    feedbacks = [feedback for feedback in feedbacks if date in feedback]
                except ValueError:
                    print("Invalid date format")
            if feedbacks:
                print("\nDate | Chef | Feedback")
                print("-----------------------------")
                for feedback in feedbacks:
                    print(feedback.strip())
            else:
                print("No feedback found")
    except FileNotFoundError:
        print("No feedback found")

def updateProfile ():
    print("\n==== Update Profile ====")
    current_username = input("Enter current username: ").strip()
    current_password = input("Enter current password: ").strip()
    user_found = False
    try:
        with open("Files/users.txt", "r") as file:
            users = file.readlines()
            
        for i, user in enumerate(users):
            username, password, role = user.strip().split(",")
            if username == current_username and password == current_password:
                user_found = True
                print("What would you like to update?")
                print("1. Username")
                print("2. Password")
                print("3. Both")
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
                break
        if user_found:
            with open("Files/users.txt", "w") as file:
                file.writelines(users)
            print("Profile updated successfully")
        else:    
            print("Invalid username or password. Update failed")
    except FileNotFoundError:
        print("No user found")



