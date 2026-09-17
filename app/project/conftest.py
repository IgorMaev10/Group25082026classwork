from pytest import fixture
from models import ShoppingCart, Item

@fixture(scope='session')
def item_1() -> Item:
    apple = Item(name="apple", price=10, quantity=1)
    return apple

@fixture(scope='class')
def shopping_cart(item_1: Item) -> ShoppingCart:
    shopping_cart_created = ShoppingCart()
    shopping_cart_created.add_item(item_1)
    return shopping_cart_created




