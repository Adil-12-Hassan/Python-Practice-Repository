# A Program to create a custom exception with a custom message.

class TemperatureError(Exception):
  
  # Constructors are special methods that are automatically called when an object is created. They are used to initialize the object's attributes and set up its initial state.

    def __init__(self, temperature):
        self.temperature = temperature


try:
    temperature = float(input("Enter temperature: "))

    if temperature < -50 or temperature > 60:
        raise TemperatureError(temperature)

    print(f"Temperature: {temperature}°C")

except TemperatureError as error:
    print(f"Invalid temperature: {error.temperature}°C")

# Explanation:
# TemperatureError stores the invalid temperature through its constructor. When the value falls outside the allowed range, the program raises the custom exception and retrieves the stored value from the exception object.

# Real-Life Use:
# Custom exceptions can carry useful information about exactly what caused an application-specific error.