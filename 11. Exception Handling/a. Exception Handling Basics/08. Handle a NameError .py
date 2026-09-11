# A Program to Handle an Undefined Variable.

try:
    print(username)

except NameError:
    print("The variable has not been defined.")

# Explanation:
# The program tries to use username before creating that variable. Python raises NameError because it cannot find the requested name. The except block catches the error and displays a message.

# Real-Life Use:
# Debugging systems can identify problems caused by incorrectly referenced variables.