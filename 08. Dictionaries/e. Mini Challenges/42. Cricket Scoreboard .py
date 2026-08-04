# A Program to display a Cricket Scoreboard.

players = {
    "Hasher":94,
    "Babar": 85,
    "Rizwan": 63,
    "Shaheen": 12
}

for player, runs in players.items():
    print(f"{player} scored {runs} runs.")

# Explanation:
# The program stores player names as dictionary keys and their runs as values. The loop visits each player and prints a formatted scoreboard. Each iteration retrieves one key-value pair until every player's score has been displayed.

# Real-Life Use:
# Scoreboard software uses similar structures to display live match statistics.