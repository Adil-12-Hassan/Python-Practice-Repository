# A Program to Play a Number Guessing Game (One Guess).

secret_number = 7

guess = int(input("\nGuess the number (1-10): "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess.")
    
# Explanation:
# In this code snippet, we have a secret number set to 7. The user is prompted to guess the number by entering an integer between 1 and 10. We then check if the user's guess matches the secret number using an if statement. If the guess is correct, we print a congratulatory message. If the guess is incorrect, we inform the user that their guess was wrong. This code provides a simple number guessing game with only one attempt.