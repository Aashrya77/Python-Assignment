#addMenuItem
def addMenuItem():
    print("\n==== Adding a menu item =====")
    category = input("Enter category: ").strip()
    item = input("Enter item: ").strip()
    price = input("Enter price: ").strip()
    
    try:
        with open("Files/menu.txt", "a") as file:
            file.write(f"\n{category},{item},{price}")
        print("Item added successfully")
    except FileNotFoundError:
        print("File not found")

#edit menu item

def editMenuItem():
    print("\n==== Editing a menu item =====")
    item_to_edit = input("Enter item to edit: ").strip()

    try:
        with open("Files/menu.txt", "r") as file:
            menu = file.readlines()

        item_found = False
        for i, line in enumerate(menu):
            category, item, price = line.strip().split(",")
            if item == item_to_edit:
                print(f"Current category: {category}, Current Price: {price}")
                new_price = input("Enter new price: ").strip()
                if new_price:
                    menu[i] = f"{category},{item},{new_price}\n"
                    item_found = True
                    break
        if item_found:
            with open("Files/menu.txt", "w") as file:
                file.writelines(menu)
            print("Item edited successfully")
        else:
            print("Item not found")
    except FileNotFoundError:
        print("File not found")

def deleteMenuItem():
    print("\n==== Deleting a menu item =====")
    item_to_delete = input("Enter item to delete: ").strip()

    try:
        with open("Files/menu.txt", "r") as file:
            menu = file.readlines()

        new_menu = [line for line in menu if item_to_delete not in line]
        if len(new_menu) < len(menu):
            with open("Files/menu.txt", "w") as file:
                file.writelines(new_menu)
            print("Item deleted successfully")
        else:
            print("Item not found")
    except FileNotFoundError:
        print("File not found")

