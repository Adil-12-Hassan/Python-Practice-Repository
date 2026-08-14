# A Program to check lottery numbers.

winning_numbers = {5, 10, 18, 27, 40, 49}
your_numbers = {3, 10, 18, 22, 40, 50}

matched = winning_numbers.intersection(your_numbers)

print("Matched Numbers:", matched)
print("Total Matches:", len(matched))

# Explanation:
# The program creates two sets: one for the winning lottery numbers and one for the user's selected numbers. The intersection() method finds the numbers that appear in both sets. Finally, the program counts how many matches were found.

# Real-Life Use:
# Lottery systems compare ticket numbers with winning numbers using similar matching techniques.