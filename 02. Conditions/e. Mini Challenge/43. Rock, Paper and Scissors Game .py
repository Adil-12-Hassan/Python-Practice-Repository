# A Program to Play Rock, Paper, Scissors Game.

player1 = input("\nPlayer 1 (rock/paper/scissors): ").lower()
player2 = input("Player 2 (rock/paper/scissors): ").lower()

if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "paper" and player2 == "rock") or \
     (player1 == "scissors" and player2 == "paper"):
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")
    
# Explanation:
# In this code snippet, we have a simple Rock, Paper, Scissors game for two players. Each player is prompted to enter their choice (rock, paper, or scissors). The input is converted to lowercase to ensure consistency. We then compare the choices using if-elif-else statements to determine the winner based on the rules of the game. If both players choose the same option, it's a tie. Otherwise, we check the winning conditions for Player 1 and declare the winner accordingly. This code provides a basic implementation of the Rock, Paper, Scissors game.