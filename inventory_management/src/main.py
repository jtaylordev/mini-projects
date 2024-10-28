from inventory import Inventory
from electronics import Electronics
from clothing import Clothing
from groceries import Groceries

# Electronics item
laptop = Electronics("Laptop", 1500, 10, warranty_period=24)

# Clothing item
t_shirt = Clothing("T-Shirt", 20, 100, size='M', material='Cotton')

# Grocery item
milk = Groceries("Milk", 2, 50, expiration_date="2023-12-31")

# Create an inventory
store_inventory = Inventory()

# Add items to inventory
store_inventory.add_item(laptop)
store_inventory.add_item(t_shirt)
store_inventory.add_item(milk)

# Show inventory before discount
print("Inventory before discount:")
store_inventory.show_inventory()

# Apply discounts
store_inventory.apply_discounts()

# Show inventory after discount
print("\nInventory after discount:")
store_inventory.show_inventory()
