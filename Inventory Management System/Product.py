'''Stock movements:

Receive shipments from suppliers
Process outbound orders (reduce stock)
Transfer inventory between locations
Adjust inventory for damage/loss/found items
Full audit trail of all movements'''
import ManagementMain
from DataValidation import DataValidation


class Product:
    def __init__(self, name = None, cost = None, sku = None, quantity: int = 0):
        self._name = name if name is not None else self.set_name()
        self._cost = cost if cost is not None else self.set_cost()
        if sku is None:
            new_sku = DataValidation.check_sku_duplicates(self.generate_sku(), ManagementMain.stores_list)
            self._sku = new_sku
        else:
            self._sku = sku
        self._quantity = quantity if quantity >= 0 else self.set_quantity()

    def __str__(self):
        return f"Product Name: {self._name}, Cost: {self.cost}, SKU: {self.sku}, Quantity: {self._quantity}"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be blank.")
        self._name = value
    @staticmethod
    def set_name():
        while not (name := input("Enter the name of the product: ")).strip():
            print("Can not be blank.")
        return name

    @property
    def cost(self):
        return self._cost / 100
    @cost.setter
    def cost(self, value):
        if value < 0:
            raise ValueError("Cost cannot be negative.")
        self._cost = value
    @staticmethod
    def set_cost():
        while not (cost := input("Enter the cost of the product: ")).strip():
            print("Can not be blank.")
        return int(cost.replace('.', ''))

    @property
    def sku(self):
        return self._sku
    @sku.setter
    def sku(self, value):
        self._sku = value
    @staticmethod
    def generate_sku():
        import random
        return "SKU" + str(random.randint(10000, 99999))

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value
    @staticmethod
    def set_quantity():
        while not (quantity := input("Enter the quantity of the product: ")).strip():
            print("Can not be blank.")
        return int(quantity)

    @staticmethod
    def update_product(product):
        print("\nWhat would you like to update?")
        print("1. Name")
        print("2. Cost")
        print("3. Quantity")
        while True:
            update_input = input("Select an option: ").strip()
            if update_input == "1":
                product.name = Product.set_name()
                print("Product name updated.")
                break
            elif update_input == "2":
                product.cost = Product.set_cost()
                print("Product cost updated.")
                break
            elif update_input == "3":
                product.quantity = Product.set_quantity()
                print("Product quantity updated.")
                break
            else:
                print("Not a valid input. Please try again.")

    @staticmethod
    def remove_product(store, sku):
        product_to_remove = next((product for product in store.store_inventory if product.sku == sku), None)
        if product_to_remove:
            store.store_inventory.remove(product_to_remove)
            print(f"Product with SKU {sku} removed from store inventory.")
            return True
        else:
            print(f"Product with SKU {sku} not found in store inventory.")
            return False