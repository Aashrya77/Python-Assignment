from manage_staff import addStaff, updateStaff, removeStaff, viewAllStaff

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

def updateProfile ():
    print("\n==== Update Profile ====")


