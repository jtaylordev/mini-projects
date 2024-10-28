from item import Item


class Electronics(Item):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    def apply_discount(self, discount):
        # Electronics have a maximum discount limit
        max_discount = 20
        if discount > max_discount:
            discount = max_discount
        super().apply_discount(discount)
