
from shopping import ShoppingCart

class TestShoppingCart:
    def test_new_cart_count(self):
        cart = ShoppingCart()
        assert cart.count_items() == 0

    def test_new_cart_price(self):
            cart = ShoppingCart()
            assert cart.total_price() == 0

    def test_add_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        assert cart.items == [{"name": "apple", "price": 1.0}]

    def test_total_price(self):
        cart = ShoppingCart()
        cart.add_item("orange", 1.5)
        cart.add_item("grape", 2.0)
        assert cart.total_price() == 3.5