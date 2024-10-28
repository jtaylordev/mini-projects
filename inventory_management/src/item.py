class Item:
    def __init__(self, name, price, quantity):
        self.__name = name
        self._price = price
        self.quantity = quantity

    def get_name(self):
        return self.__name

    def get_price(self):
        return self._price

    def apply_discount(self, discount):
        self._price = self._price * discount / 100

