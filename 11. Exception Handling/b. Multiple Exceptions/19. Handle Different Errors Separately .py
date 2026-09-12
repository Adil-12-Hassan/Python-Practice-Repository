# A Program to Handle Different Errors with Different Messages.

try:
    numbers = [10, 20, 30]
    index = int(input("Enter an index: "))

    value = numbers[index]
    result = 100 / value

    print(f"Result: {result}")

except ValueError:
    print("Please enter an integer index.")

except IndexError:
    print("The index does not exist.")

except ZeroDivisionError:
    print("The selected value cannot be zero.")

# Explanation:
# The program converts the input, accesses a list element, and then performs division. Each operation can produce a different exception, so each error receives its own except block and message.

# Real-Life Use:
# Larger programs often perform several operations in sequence and need precise error handling for each possible failure.