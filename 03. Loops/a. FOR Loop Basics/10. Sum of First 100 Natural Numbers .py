# A Program to Print the Sum of the First 100 Natural Numbers.

total = 0

for number in range(1, 101):
    total += number

print(f"Sum = {total}")

# Explanation:
# This code snippet uses a for loop to calculate the sum of the first 100 natural numbers. The range function generates a sequence of numbers starting from 1 up to (but not including) 101. Inside the loop, the current number is added to the total variable using the `+=` operator. After the loop completes, the print function outputs the final sum to the console in a formatted string. This demonstrates how to use a for loop to perform cumulative calculations on a sequence of numbers.