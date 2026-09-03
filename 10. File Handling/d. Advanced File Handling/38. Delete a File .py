# A Program to Delete a File.

import os

file_name = "old_file.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted successfully.")
else:
    print("The file does not exist.")

# Explanation:
# os.remove() deletes a file from the computer. The program first checks whether the file exists before attempting to remove it. This prevents the program from trying to delete a file that is not present.

# Real-Life Use:
# Automated systems can delete temporary files, outdated reports, cached data, or files that are no longer required.