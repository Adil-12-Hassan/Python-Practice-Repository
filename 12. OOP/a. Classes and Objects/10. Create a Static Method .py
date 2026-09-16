# A Program to create and use a static method

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


result = Calculator.add(10, 20)

print(f"Result: {result}")


# Explanation:
# add() is defined as a static method using @staticmethod. It does not require self or cls because it does not need instance or class data. The method simply receives two numbers and returns their sum. It can be called directly using the Calculator class.

# Real-Life Use:
# Static methods are useful for utility operations related to a class, such as calculations, validation, formatting, or data conversion.