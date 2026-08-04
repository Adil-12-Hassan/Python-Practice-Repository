# A Program to Handle Missing Keys safely.

student = {
    "name": "Hasher",
    "age": 20
}

print(student.get("course", "Key Not Found"))

# Explanation:
# The program creates a dictionary that does not contain the key "course". Instead of accessing the key directly, it uses the get() method with a default value. Python searches for the requested key. Since the key does not exist, get() returns the default message "Key Not Found" instead of producing an error. This makes programs safer and more reliable.

# Real-Life Use:
# The get() method is commonly used when reading optional data from APIs, configuration files, databases, and user input where some information may be missing.