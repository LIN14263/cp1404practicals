"""
Set MINIMUM_LENGTH to 8
Output "Enter your password(more than 8 numbers or alphabets):"
Get user input and store it in variable password
Set length to the length of password
While length < MINIMUM_LENGTH
    Output "Unqualified password"
    Output "Enter your password(more than 8 numbers or alphabets):"
    Get user input and update variable password
    Set length to the length of password
Output "*" repeated length times
"""
MINIMUM_LENGTH = 8
password = input("Enter your password(more than 8 numbers or alphabets):")
length = len(password)
while length < MINIMUM_LENGTH:
        print("Unqualified password")
        password = input("Enter your password(more than 8 numbers or alphabets):")
        length = len(password)
print("*" * length)