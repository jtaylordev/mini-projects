from item import Item


class Clothing(Item):
    def __init__(self, name, price, quantity, size, material):
        super().__init__(name, price, quantity)
        self.size = size
        self.material = material
