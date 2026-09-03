# A Program to Check Whether a File Exists.

import os

file_name = "sample.txt"

if os.path.exists(file_name):
    print("The file exists.")
else:
    print("The file does not exist.")

# Explanation:
# The os module provides functions for interacting with the operating system. os.path.exists() checks whether the specified file or path exists. It returns True if the file exists and False otherwise.

# Real-Life Use:
# Programs can check whether a configuration file, database file, or user-created file exists before trying to access it.