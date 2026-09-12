class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart():
    def __init__(self):
        self.items = []

    def add_item(self, item: Item) -> None:
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.quantity += item.quantity
                existing_item.price += item.price
                return

        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        if item in self.items:
            self.items.remove(item)

    def get_total(self, total_price: float = 0) -> float:
        for item in self.items:
            total_price += item.price * item.quantity
        return total_price
