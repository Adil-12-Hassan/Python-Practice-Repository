# A Program to simulate a Simple Banking System.

account = {
    "Name": "Hasher",
    "Balance": 5000
}

while True:

    print("\n===== Banking Menu =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        amount = float(input("Enter Deposit Amount: "))
        account["Balance"] += amount

    elif choice == "2":

        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= account["Balance"]:
            account["Balance"] -= amount
        else:
            print("Insufficient Balance!")

    elif choice == "3":
        print("Current Balance:", account["Balance"])

    elif choice == "4":
        print("Thank You!")
        break

# Explanation:
# The program creates a dictionary named 'account' to store the account holder's name and current balance. The while loop repeatedly displays the banking menu. Depending on the user's choice, Python updates the balance by adding deposits or subtracting withdrawals. Before withdrawing money, the program checks whether enough balance is available. The updated balance remains stored in the dictionary throughout the program, showing how dictionaries can maintain and modify real-world data.

# Real-Life Use:
# Banking software uses similar data structures to manage customer accounts, balances, deposits, withdrawals, and transactions.