class ShoppingCart:
    def __init__(self):
            self.items = []

    def add_item(self, name, price):
           self.items.append({"name": name, "price": price})

    def total_price(self):
        return sum(item["price"] for item in self.items)

    def count_items(self):
        return len(self.items)

# CartA = ShoppingCart()
# CartB = ShoppingCart()

# CartA.add_item("Apple", 1)
# CartA.add_item("Banana", 2)

# CartB.add_item("Orange", 2)
# CartB.add_item("Grapes", 3)

# print(f"Cart A Items: {[item['name'] for item in CartA.items]}")
# print(f"Cart A Total: {CartA.total_price()} THB")

# print(f"Cart B Items: {[item['name'] for item in CartB.items]}")
# print(f"Cart B Total: {CartB.total_price()} THB")
