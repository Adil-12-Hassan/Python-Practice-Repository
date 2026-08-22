# A Program to Display the Contents of a file with Line Numbers.

file = open("message.txt", "r")

line_number = 1

for line in file:
    print(f"{line_number}: {line.strip()}")
    line_number += 1

file.close()

# Explanation:
# The file is opened in read mode.
# line_number starts from 1 because the first line should be numbered 1. The for loop processes each line of the file.
# Each line is displayed together with its number.
# line_number is increased after every iteration.

# Real-Life Use:
# Numbered lines are useful when displaying source code, logs, reports, configuration files, and debugging information.