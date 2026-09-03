# A Program to Read File Content from a Specific Position.

with open("sample.txt", "r") as file:

    file.seek(9)

    remaining_data = file.read()

    print("Data from position 10:")
    print(remaining_data)

# Explanation:
# seek(9) moves the file cursor to position 9. The read() method then reads everything from that position until the end of the file. This demonstrates how seek() and read() can work together.

# Real-Life Use:
# Reading from a specific position can be useful when processing large files or continuing work from a known location.