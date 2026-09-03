# A Program to Write and Read Binary Data.

data = b"Python Binary Data"

with open("data.bin", "wb") as file:
    file.write(data)

with open("data.bin", "rb") as file:
    content = file.read()

print("Binary data:", content)

# Explanation:
# Binary files store data as bytes instead of normal text characters. The "wb" mode opens a file for writing binary data, while "rb" opens it for reading binary data. The b prefix creates a bytes object.

# Real-Life Use:
# Binary file handling is used for images, audio, videos, executable files, and other data that should be handled as raw bytes.