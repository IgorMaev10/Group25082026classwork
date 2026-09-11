class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart():
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.quantity += item.quantity
                existing_item.price += item.price
                print(self.items)            # fix later
                return
        self.items.append(item)
        print(self.items)                    # fix later
shopping_cart = ShoppingCart()
shopping_cart.add_item(Item("Breakfast", 5.00, 1))

