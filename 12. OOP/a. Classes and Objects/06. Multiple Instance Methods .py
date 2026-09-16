# A Program to create multiple methods inside a class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} started.")

    def stop(self):
        print(f"{self.brand} {self.model} stopped.")

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


car = Car("Toyota", "Corolla")

car.show_details()
car.start()
car.stop()


# Explanation:
# A Car object is created with brand and model information. show_details(), start(), and stop() are instance methods. Each method uses self to access the same object's attributes. The methods are called through the car object in sequence.

# Real-Life Use:
# A real application can model a car with actions such as starting, stopping, accelerating, braking, and displaying its information.