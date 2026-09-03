# A Program to Analyze Quiz Scores using a Dictionary.

scores = {
    "Ali": 85,
    "Ahmed": 72,
    "Sara": 94,
    "Usman": 68
}

highest_score = max(scores.values())
lowest_score = min(scores.values())
average_score = sum(scores.values()) / len(scores)

print(f"\nHighest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Average Score: {average_score:.2f}")

# Explanation:
# The scores dictionary stores student names as keys and their scores as values. values() provides all the scores, which are then used with max(), min(), sum(), and len() to calculate useful statistics.

# Real-Life Use:
# Teachers and learning platforms can use similar calculations to analyze student performance and generate score reports.