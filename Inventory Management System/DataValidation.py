'''Data validation:

Prevent negative stock levels
Validate SKU uniqueness
Check for sufficient stock before shipments
Handle concurrent stock updates safely'''

class DataValidation:
    @staticmethod
    def check_stock(product):
        try:
            if getattr(product, 'quantity', None) > 0:
                return True
            else:
                print(f"Insufficient stock for product: {getattr(product, 'name', 'Unknown')}")
                return False
        except Exception:
            return False

    @staticmethod
    def check_sku(product, inventory):
        try:
            for item in inventory:
                print(f"Checking SKU: {getattr(item, 'sku', 'Unknown')} against {getattr(product, 'sku', 'Unknown')}")
                while getattr(product, 'sku', None) == item.sku:
                    print(f"Duplicate SKU found: {getattr(product, 'name', 'Unknown')}")
                    print(f"Generating new sku!")
                    product.sku = product.generate_sku()
                    return False
            return True
        except Exception:
            return False

