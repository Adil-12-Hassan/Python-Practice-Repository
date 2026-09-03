# A Program to Calculate the Total Cost of a Shopping cart.

cart = {
    "Laptop": 80000,
    "Mouse": 2500,
    "Keyboard": 4500,
    "Headphones": 6000
}

total = 0

for item, price in cart.items():

    print(f"{item}:  Rs.{price}")
    total += price

print(f"\nTotal:  Rs.{total}")

# Explanation:
# The cart dictionary stores product names as keys and their prices as values. The loop processes every product and adds its price to the total variable. After all products are processed, the final shopping amount is displayed.

# Real-Life Use:
# E-commerce websites use similar logic to calculate the total price of products added to a customer's shopping cart.