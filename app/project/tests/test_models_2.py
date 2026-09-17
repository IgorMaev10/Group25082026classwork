from models import Item, ShoppingCart

class TestShoppingCart:

    def test_adding_item(self, shopping_cart:ShoppingCart, item_1:Item):
        assert shopping_cart.items[0].name == "apple"
        assert shopping_cart.items[0].price == 10
        assert shopping_cart.items[0].quantity == 1

    def test_removing_item(self, shopping_cart:ShoppingCart, item_1:Item):
        shopping_cart.remove_item(item_1)
        assert len(shopping_cart.items) == 0

    def test_get_total(self, shopping_cart:ShoppingCart, item_1:Item):
        shopping_cart.add_item(item_1)
        assert shopping_cart.get_total() == 10
