# A Program to use a frozenset as a dictionary key.

data = {
    frozenset({"Python", "AI"}): "Learning Path"
}

print(data)

# Explanation:
# The program creates a dictionary whose key is a frozenset. Python allows this because frozensets are immutable and therefore hashable. Normal sets cannot be used as dictionary keys because their contents can change. The dictionary stores the frozenset as the key and its associated value.

# Real-Life Use:
# Frozensets are used as dictionary keys when representing fixed combinations, permissions, or unique groups of values.