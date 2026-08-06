# A Program to Check whether two Sets are Disjoint.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

result = set1.isdisjoint(set2)

print("Are the sets disjoint?\n", result)

# Explanation:
# The program creates two sets and checks them using the isdisjoint() method. Python compares both sets to see whether they share any common elements. If no common element exists, the method returns True. If even one element is shared, it returns False.

# Real-Life Use:
# This method is useful for checking whether two groups, schedules, or collections have anything in common before combining or comparing them.