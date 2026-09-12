from models import Item, ShoppingCart

class TestShoppingCart:

    def test_adding_item(self):
        apple = Item(name="apple", price=10, quantity=1)
        shopping_cart = ShoppingCart()
        shopping_cart.add_item(apple)
        assert shopping_cart.items[0].name == "apple"
        assert shopping_cart.items[0].price == 10
        assert shopping_cart.items[0].quantity == 1

    def test_removing_item(self):
        apple = Item(name="apple", price=10, quantity=1)
        shopping_cart = ShoppingCart()
        shopping_cart.add_item(apple)
        shopping_cart.remove_item(apple)
        assert len(shopping_cart.items) == 0

    def test_get_total(self):
        apple = Item(name="apple", price=10, quantity=1)
        orange = Item(name="orange", price=20, quantity=1)
        shopping_cart = ShoppingCart()
        shopping_cart.add_item(apple)
        shopping_cart.add_item(orange)
        assert shopping_cart.get_total() == 30

