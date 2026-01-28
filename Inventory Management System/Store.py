'''Inventory tracking:

Track stock levels across multiple warehouse locations
Record inventory transactions (receive, ship, adjust, transfer)
Support batch/lot tracking with expiration dates
Handle stock reservations (items on hold for orders)
Low stock alerts and automatic reorder suggestions'''
from DataValidation import DataValidation

class Store:
    def __init__(self, store_name = None, store_number: int = 0):
        self._store_name = store_name if store_name is not None else self.set_store_name()
        self.store_inventory = []
        if store_number == 0:
            import ManagementMain
            new_store_number = DataValidation.check_store_number_duplicates(Store.generate_store_number(), ManagementMain.stores_list)
            self._store_number = new_store_number
        else:
            self._store_number = store_number


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

    @property
    def store_number(self):
        return self._store_number
    @staticmethod
    def generate_store_number():
        import random
        return random.randint(1000, 9999)

    @staticmethod
    def send_items(sending_store, receiving_store, sku, quantity):
        try:
            from Product import Product
            print(sku)
            print(str(sending_store))
            print(str(receiving_store))

            #Finds the product in the sending store inventory
            sending_product = next((product for product in sending_store.store_inventory if product.sku == sku), None)
            print(f"{sending_product}")
            DataValidation.check_stock(sending_product, quantity)
            if sending_product.quantity - quantity > 0:
                sending_product.quantity -= quantity
            else:
                print(f"Not enough stock to be able to move to new store.")
                return False

            #Finds the product in the receiving store inventory
            receiving_product = next((product for product in receiving_store.store_inventory if product.sku == sku), None)
            if receiving_product:
                print("Product found in receiving store. Updating quantity.")
                receiving_product.quantity += quantity
            else:
                print("Product not found in receiving store. Adding new product.")
                receiving_store.store_inventory.append(Product(sending_product.name, sending_product.cost, sending_product.sku,quantity))
            return True
        except Exception as e:
            print(f"Error when trying to send items: {e}")
            return False