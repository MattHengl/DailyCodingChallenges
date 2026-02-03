'''Data validation:
Prevent negative stock levels
Validate SKU uniqueness
Check for sufficient stock before shipments
Handle concurrent stock updates safely'''


class DataValidation:
    @staticmethod
    def check_stock(product, quantity):
        try:
            product_sku = getattr(product, 'sku', 'Unknown')
            product_quantity = getattr(product, 'quantity', 0)
            print(f"{product_sku} - {product_quantity}")
            if product is None:
                print(f"{product_sku} not found in sending store inventory.")
                return False
            if product_quantity < quantity or product_quantity < 0:
                print(f"Not enough {product_sku} in inventory to send.")
                return False
            return True
        except Exception as e:
            print(f"There was an error when checking stock: {e}")
            return False

    @staticmethod
    def check_sku_duplicates(searching_sku, store_list):
        try:
            print(f"Searching for SKU value {searching_sku}")
            for store in store_list:
                print(f"Searching store {store.store_name}")
                for product in store.store_inventory:
                    if product.sku == searching_sku:
                        print(f"Duplicate SKU number found with product {product.name} - {product.sku}")
                        print(f"Assigning new SKU number.")
                        from Product import Product
                        return DataValidation.check_sku_duplicates(Product.generate_sku(), store_list)
            print(f"No Duplicate SKUs found for {searching_sku}")
            return searching_sku
        except Exception as e:
            print(f"Error while searching for sku in store list: {e}")
            return False


    @staticmethod
    def check_store_number_duplicates(searching_store_number, store_list):
        try:
            print(f"Searching for store number {searching_store_number}")
            for store in store_list:
                print(f"Searching store {store.store_name}")
                if store.store_number == searching_store_number:
                    print(f"Duplicate store number found {store.store_name} - {store.store_number}")
                    print(f"Assigning new store number.")
                    from Store import Store
                    return DataValidation.check_store_number_duplicates(Store.generate_store_number(), store_list)
            print(f"No Duplicate store number found for {searching_store_number}")
            return searching_store_number
        except Exception as e:
            print(f"Error while searching for store number in store list: {e}")
            return False