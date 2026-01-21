'''Inventory tracking:

Track stock levels across multiple warehouse locations
Record inventory transactions (receive, ship, adjust, transfer)
Support batch/lot tracking with expiration dates
Handle stock reservations (items on hold for orders)
Low stock alerts and automatic reorder suggestions'''
from Product import Product

class Store:
    def __init__(self, store_name = None):
        self._store_name = store_name if store_name is not None else self.set_store_name()
        self.store_inventory = []

    def __str__(self):
        return_string = f"\nStore Name: {self._store_name} - "
        for item in self.store_inventory:
            return_string += f"\n{str(item)}"
        return return_string

    @property
    def store_name(self):
        return self._store_name
    @staticmethod
    def set_store_name():
        while not (store_name := input("Enter the name of your store: ")).strip():
            print("Can not be blank.")
        return store_name

    @staticmethod
    def send_items(sending_store, receiving_store, sku, quantity):
        print(sku)
        print(str(sending_store))
        print(str(receiving_store))

        #Finds the product in the sending store inventory
        sending_product = next((product for product in sending_store.store_inventory if product.sku == sku), None)
        if sending_product is None:
            print(f"{sku} not found in sending store inventory.")
            return False
        if sending_product.quantity < quantity:
            print(f"Not enough {sku} in inventory to send.")
            return False
        sending_product.quantity -= quantity

        #Finds the product in the receiving store inventory
        receiving_product = next((product for product in receiving_store.store_inventory if product.sku == sku), None)
        if receiving_product:
            print("Product found in receiving store. Updating quantity.")
            receiving_product.quantity += quantity
        else:
            print("Product not found in receiving store. Adding new product.")
            receiving_store.store_inventory.append(Product(sending_product.name, sending_product.cost, sku, quantity))
        return True

    @staticmethod
    def look_for_store(wanted_store, stores_list):
        return any(store.store_name.lower() == wanted_store for store in stores_list)