'''Reporting and analytics:

Current stock levels by product/location
Inventory value calculations
Movement history and transaction logs
Products below reorder point
Slow-moving vs fast-moving inventory analysis
Stock turnover rates
Forecasting based on historical data'''

class Reporting:
    @staticmethod
    def current_stock(inventory):
        if inventory is not None and len(inventory) > 0:
            print(f"Current amount of items in the store inventory: {len(inventory)}")
            for item in inventory:
                print(f"{str(item)}")
            return True
        else:
            print("There is no inventory to report.")
            return False
