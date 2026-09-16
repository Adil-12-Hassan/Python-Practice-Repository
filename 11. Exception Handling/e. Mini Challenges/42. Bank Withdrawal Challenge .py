# A Program to safely process a bank withdrawal.

class WithdrawalError(Exception):
    pass


balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise WithdrawalError("Withdrawal amount must be positive.")

    if amount > balance:
        raise WithdrawalError("Insufficient balance.")

    balance -= amount

except ValueError:
    print("Please enter a valid amount.")

except WithdrawalError as error:
    print(f"Error: {error}")

else:
    print(f"Withdrawal successful.")
    print(f"Remaining balance: {balance}")

# Explanation:
# The program receives a withdrawal amount and checks whether it is positive and within the available balance. WithdrawalError handles invalid banking rules. The balance is updated only when all checks succeed.

# Real-Life Use:
# Banking applications use validation and custom exceptions for transactions.