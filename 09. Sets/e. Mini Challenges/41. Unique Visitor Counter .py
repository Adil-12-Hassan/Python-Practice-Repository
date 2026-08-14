# A Program to count unique website visitors.

visitors = {
    "192.168.1.10",
    "192.168.1.15",
    "192.168.1.10",
    "192.168.1.20"
}

print("Unique Visitors:", len(visitors))

# Explanation:
# The program stores visitor IP addresses inside a set. If the same visitor appears multiple times, Python automatically removes duplicate entries. The len() function then counts the number of unique visitors.

# Real-Life Use:
# Websites use this technique to count unique visitors instead of total visits.