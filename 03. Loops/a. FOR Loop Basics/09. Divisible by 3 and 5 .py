# A Program to Print All Numbers Divisible by Both 3 and 5 Between 1 and 100.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number)
        
# Explanation:
# This code snippet uses a for loop to iterate through numbers from 1 to 100. The range function generates a sequence of numbers starting from 1 up to (but not including) 101. Inside the loop, an if statement checks if the current number is divisible by both 3 and 5 using the modulus operator `%`. If the condition is true, the print function outputs the current number to the console. This demonstrates how to use a for loop in combination with a conditional statement to filter and display specific numbers from a sequence.