# A Program to Check Whether a File Exists.

import os

file_name = "message.txt"

if os.path.exists(file_name):
    print("File exists.")
else:
    print("File does not exist.")

# Explanation:
# The os module provides functions for interacting with the operating system.
# os.path.exists() checks whether the specified file or path exists. The if statement then displays the appropriate message.

# Real-Life Use:
# Programs often check whether a file exists before trying to read, modify, or delete it.