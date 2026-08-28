# A Program to Append Multiple Lines to a File.

new_languages = [
    "Go",
    "Rust",
    "Kotlin"]

with open("sample.txt", "a") as file:

    for language in new_languages:
        file.write(language + "\n")

print("Multiple lines appended successfully.")

# Explanation:
# The new_languages list stores multiple values. The for loop processes each language one by one and writes it to the file. The "\n" places every new language on a separate line. Append mode keeps the existing file content.

# Real-Life Use:
# This approach is useful when a program needs to add multiple new records to an existing file.