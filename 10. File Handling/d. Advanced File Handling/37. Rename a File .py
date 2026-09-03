# A Program to Rename a File.

import os

old_name = "sample.txt"
new_name = "renamed_sample.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully.")
else:
    print("The file does not exist.")

# Explanation:
# os.rename() changes the name of an existing file. The program first checks whether the original file exists. If it does, the file is renamed from old_name to new_name.

# Real-Life Use:
# File renaming is useful in automation systems that organize documents, reports, downloads, images, or generated files.