# A Program to create a property getter and setter

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Price cannot be negative.")


product = Product(1000)

print(product.price)

product.price = 1200
print(product.price)

product.price = -500


# Explanation:
# The price property provides controlled access to __price. The getter returns the current price. The setter runs automatically when product.price is assigned. The setter validates the value before storing it.

# Real-Life Use:
# Property setters are useful for validating prices, quantities, ages, account limits, and other values before updating an object.