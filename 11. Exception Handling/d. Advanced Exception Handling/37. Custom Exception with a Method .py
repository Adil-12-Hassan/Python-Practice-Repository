# A Program to create a custom exception with additional information.

class BalanceError(Exception):

    def show_message(self):
        return "Insufficient balance."


try:
    balance = 500
    
    withdrawal = int(input("Enter withdrawal amount: "))

    if withdrawal > balance:
        raise BalanceError()

    print(f"Remaining balance: {balance - withdrawal}")

except BalanceError as error:
    print(f"Error: {error.show_message()}")

# Explanation:
# BalanceError inherits from Exception and defines a custom method called show_message(). If the withdrawal is greater than the available balance, the program raises BalanceError and uses its method to display the message.

# Real-Life Use:
# Banking systems can use custom exceptions to represent specific business rules such as insufficient funds.