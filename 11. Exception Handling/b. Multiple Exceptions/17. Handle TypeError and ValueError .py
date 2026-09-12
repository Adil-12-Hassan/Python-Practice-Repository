# A Program to Handle TypeError and ValueError.

try:
    number = int(input("Enter a number: "))
    result = number + "10"
    print(result)

except ValueError:
    print("The input must be a valid integer.")

except TypeError:
    print("The values have incompatible data types.")

# Explanation:
# The input is first converted into an integer. If conversion fails, ValueError occurs. If conversion succeeds, Python then tries to add an integer and a string, which raises TypeError.

# Real-Life Use:
# Programs that process data from different sources need to handle unexpected data types and invalid conversions.