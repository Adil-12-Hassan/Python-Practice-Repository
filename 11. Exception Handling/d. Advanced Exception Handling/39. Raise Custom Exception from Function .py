# A Program to raise a custom exception from a function.

class WithdrawalError(Exception):
    pass


def withdraw(balance, amount):

    if amount <= 0:
        raise WithdrawalError("Withdrawal amount must be positive.")

    if amount > balance:
        raise WithdrawalError("Insufficient balance.")

    return balance - amount


try:
    balance = 1000
    amount = int(input("Enter withdrawal amount: "))

    remaining_balance = withdraw(balance, amount)

    print(f"Remaining balance: {remaining_balance}")

except WithdrawalError as error:
    print(f"Error: {error}")

# Explanation:
# The withdraw() function checks the requested amount before performing the calculation. It raises WithdrawalError when the amount is invalid or greater than the balance. The main program catches the custom exception.

# Real-Life Use:
# Functions in large applications can use custom exceptions to report specific business-rule violations to the calling code.