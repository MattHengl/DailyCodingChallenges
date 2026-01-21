import ManagementMain
from Product import Product
from Reporting import Reporting
from Store import Store


def display_main_menu():
    print("=== Inventory Management System ===")
    print("1. Manage Locations")
    print("2. Manage Products")
    print("3. Send Product Between Locations")
    print("4. View Reports")
    print("5. Exit")
    handle_menu_option()

def handle_menu_option():
    while True:
        menu_input = input("What action would you like to perform? ").strip()
        if menu_input == "1":
            display_store_menu()
        elif menu_input == "2":
            display_product_menu()
        elif menu_input == "3":
            sending_store, receiving_store, sku, quantity = get_info_for_send_products()
            Store.send_items(sending_store, receiving_store, sku, quantity)
        elif menu_input == "4":
            view_reports()
        elif menu_input == "5":
            print("Exiting the system. Goodbye!")
            exit()
        else:
            print("Not a valid input. Please try again.")

def display_store_menu():
    print("\nWhat would you like to do with locations?")
    print("1. Add Location")
    print("2. Update Location")
    print("3. Delete Location")
    print("4. View Locations")
    print("5. Back to Main Menu")
    handle_store_menu()

def handle_store_menu():
    while True:
        store_menu_input = input("Please select an options from the menu: ").strip()
        if store_menu_input == "1":
            ManagementMain.stores_list.append(Store())
            display_main_menu()
            break
        elif store_menu_input == "2":
            Store.set_store_name()
        elif store_menu_input == "3":
            store_to_remove = input("Enter the name of the store to remove: ").strip()
            store_instance = get_and_check_for_store(store_to_remove)
            if store_instance is not None:
                ManagementMain.stores_list.remove(store_instance)
                print(f"Store '{store_to_remove}' has been removed.")
        elif store_menu_input == "4":
            display_stores()
        elif store_menu_input == "5":
            display_main_menu()
            break
        else:
            print("Not a valid input. Please try again.")



def display_product_menu():
    display_stores()
    current_store = get_and_check_for_store(input("Enter the name of the store you are looking for: ").strip())
    print("\nWhat would you like to do within this location?")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. View Products")
    print("5. Back to Main Menu")
    handle_product_menu(current_store)

def handle_product_menu(current_store):
    while True:
        if current_store is not None:
            product_input = input("Select an option: ").strip()
            if product_input == "1":
                current_store.store_inventory.append(Product())
            elif product_input == "2":
                Product.update_product(input("Enter the name of the store you are looking for: ").strip())
            elif product_input == "3":
                Reporting.current_stock(current_store)
                Product.remove_product(current_store, input("Enter the SKU of the product to remove: ").strip())
            elif product_input == "4":
                Reporting.current_stock(current_store.store_inventory)
            elif product_input == "5":
                display_main_menu()
                break
            else:
                print("Not a valid input. Please try again.")
        else:
            print("Need a store to progress. Returning to locations menu.")
            display_product_menu()

def get_info_for_send_products():
    sending_store = get_and_check_for_store(input("Enter the name of the sending store: ").strip())
    receiving_store = get_and_check_for_store(input("Enter the name of the receiving store: ").strip())
    sku = input("Enter the SKU of the product to send: ").strip()
    quantity = int(input("Enter the quantity to send: ").strip())
    return sending_store, receiving_store, sku, quantity


def get_and_check_for_store(wanted_store):
    if Store.look_for_store(wanted_store.lower(), ManagementMain.stores_list):
        print(f"{wanted_store} found.")
        current_store = next((store for store in ManagementMain.stores_list if store.store_name.lower() == wanted_store.lower()), None)
        return current_store
    else:
        print("Store not found.")
        return None

def view_reports():
    print("No.")

def display_stores():
    print("\nCurrent Locations:")
    for store in ManagementMain.stores_list:
        print(f"- {store.store_name}")