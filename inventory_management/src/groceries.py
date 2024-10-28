from item import Item


class Groceries(Item):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def apply_discount(self, discount):
        # Groceries have a different discount calculation
        super().apply_discount(discount * 1.5)  # 50% more discount
