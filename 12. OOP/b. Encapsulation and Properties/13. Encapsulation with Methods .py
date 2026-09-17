# A Program to protect object data using methods

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def show_balance(self):
        print(f"Balance: {self.__balance}")


account = BankAccount("Ali", 5000)

account.deposit(2000)
account.withdraw(1000)
account.show_balance()


# Explanation:
# __balance stores the account balance internally. deposit() and withdraw() control how the balance is changed. Invalid amounts are ignored instead of changing the balance. This keeps the object's internal state controlled through methods.

# Real-Life Use:
# Encapsulation is commonly used in banking, shopping carts, user accounts, and other systems where data needs controlled access.