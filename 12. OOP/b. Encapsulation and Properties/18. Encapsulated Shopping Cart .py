# A Program to create an encapsulated shopping cart

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def show_items(self):
        print("Cart Items:")
        for item in self.__items:
            print(item)


cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

cart.remove_item("Mouse")
cart.show_items()


# Explanation:
# __items stores the shopping cart data internally.
# add_item() adds products to the list.
# remove_item() removes a product when it exists.
# show_items() provides controlled access for displaying the cart.

# Real-Life Use:
# Encapsulation is useful in e-commerce systems where cart data should be modified through defined operations rather than freely.