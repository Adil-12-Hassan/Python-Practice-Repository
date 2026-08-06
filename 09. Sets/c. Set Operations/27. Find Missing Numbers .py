# A Program to find Missing Numbers between two Sets.

expected = {1, 2, 3, 4, 5, 6}
received = {1, 2, 4, 6}

missing = expected.difference(received)

print("Missing Numbers:", missing)

# Explanation:
# The program creates two sets. The first set contains all expected values, while the second contains the values that were actually received. The difference() method compares both sets and returns only the elements that exist in the first set but not in the second.

# Real-Life Use:
# This method is useful for identifying missing attendance records, missing files, incomplete survey responses, or absent students.