# A Program to Compare Inventory between two stores.

store1 = {"Keyboard", "Mouse", "Monitor", "Printer"}
store2 = {"Mouse", "Printer", "Laptop", "Speaker"}

common_items = store1.intersection(store2)
unique_items = store1.symmetric_difference(store2)

print("Common Products:", common_items)
print("Unique Products:", unique_items)

# Explanation:
# The program compares the inventories of two stores. The intersection() method finds products available in both stores, while the symmetric_difference() method identifies products available in only one store. This provides a quick comparison of both inventories.

# Real-Life Use:
# Businesses compare inventories across multiple warehouses or branches using similar techniques.