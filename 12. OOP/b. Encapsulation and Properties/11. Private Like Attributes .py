# A Program to use a private-like instance attribute

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        print(f"Balance: {self.__balance}")


account = BankAccount("Ali", 5000)

print(account.owner)
account.show_balance()


# Explanation:
# owner is a normal public instance attribute.
# __balance uses double underscores, making it name-mangled by Python. The balance is accessed inside the class through show_balance(). Python does not provide strict private access like some languages, but double underscores help prevent accidental direct access.

# Real-Life Use:
# Private-like attributes are useful for sensitive object state, such as bank balances, passwords, or internal configuration values.