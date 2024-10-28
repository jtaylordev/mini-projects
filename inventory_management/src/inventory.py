class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def apply_discounts(self):
        for item in self.items:
            item.apply_discount(10)  # Applying a 10% discount to all items

    def show_inventory(self):
        for item in self.items:
            print(f"Item: {item.get_name()}, Price: {item.get_price()}, Quantity: {item.quantity}")
