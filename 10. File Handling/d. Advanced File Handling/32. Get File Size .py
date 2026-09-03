# A Program to Find the Size of a File.

import os

file_name = "sample.txt"

if os.path.exists(file_name):
    size = os.path.getsize(file_name)
    print(f"File size: {size} bytes")
else:
    print("The file does not exist.")

# Explanation:
# os.path.getsize() returns the size of a file in bytes. The program first checks whether the file exists so that it does not try to get the size of a missing file.

# Real-Life Use:
# File size checking is useful when managing storage, validating uploads, or making sure a file does not exceed a required size limit.