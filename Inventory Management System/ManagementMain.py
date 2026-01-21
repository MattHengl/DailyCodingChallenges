'''Product management:

Add/update/delete products with SKU, name, description, price, category
Track multiple attributes (size, color, brand, supplier)
Support product variants (same product, different sizes/colors)
Set reorder points and optimal stock levels


Inventory tracking:

Track stock levels across multiple warehouse locations
Record inventory transactions (receive, ship, adjust, transfer)
Support batch/lot tracking with expiration dates
Handle stock reservations (items on hold for orders)
Low stock alerts and automatic reorder suggestions


Stock movements:

Receive shipments from suppliers
Process outbound orders (reduce stock)
Transfer inventory between locations
Adjust inventory for damage/loss/found items
Full audit trail of all movements


Reporting and analytics:

Current stock levels by product/location
Inventory value calculations
Movement history and transaction logs
Products below reorder point
Slow-moving vs fast-moving inventory analysis
Stock turnover rates
Forecasting based on historical data


Data validation:

Prevent negative stock levels
Validate SKU uniqueness
Check for sufficient stock before shipments
Handle concurrent stock updates safely



Key concepts you'll practice:

Complex object relationships (Products, Locations, Transactions)
Transaction logging and audit trails
Business rule validation and constraints
Aggregate calculations and reporting
DateTime handling for expiration tracking
LINQ for complex queries and analytics
Data consistency and integrity
State management for reservations

Bonus features:

Barcode generation for products
Import/export functionality (CSV)
Simple supplier management
Purchase order creation'''
import Menu
from Store import Store

try:
    stores_list = [Store("Main Warehouse"), Store("Downtown Store")]
    if __name__ == "__main__":
        Menu.display_main_menu()
except Exception as e:
    print(f"An error occurred: {e}")