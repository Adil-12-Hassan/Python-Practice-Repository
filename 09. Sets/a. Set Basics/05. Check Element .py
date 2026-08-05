# A Program to check whether an Element exists in a Set.

fruits = {"Apple", "Banana", "Mango"}

fruit = input("Enter a fruit: ")

if fruit in fruits:
    print("Element Found!")
else:
    print("Element Not Found!")

# Explanation:
# The program asks the user to enter a fruit name. The entered value is stored in the variable 'fruit'. The 'in' operator checks whether that value exists inside the set. If Python finds the element, the condition becomes True and the first message is printed. Otherwise, the else block executes.

# Real-Life Use:
# Membership checking is commonly used to verify usernames, product IDs, permissions, and registered email addresses.