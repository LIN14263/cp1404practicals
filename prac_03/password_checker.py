"""
MIN_LENGTH ← 2
MAX_LENGTH ← 6
IS_SPECIAL_CHARACTER_REQUIRED ← true
SPECIAL_CHARACTERS ← "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

Procedure main
    Print "Please enter a valid password"
    Print "Your password must be between " + MIN_LENGTH + " and " + MAX_LENGTH + " characters, and contain:"
    Print "\t1 or more uppercase characters"
    Print "\t1 or more lowercase characters"
    Print "\t1 or more numbers"
    If IS_SPECIAL_CHARACTER_REQUIRED
        Print "\tand 1 or more special characters: " + SPECIAL_CHARACTERS
    End if
    password ← Prompt user ">"
    While Not is_valid_password(password)
        Print "Invalid password!"
        password ← Prompt user ">"
    End while
    Print "Your " + Length(password) + "-character password is valid: " + password
End procedure

Function is_valid_password(password)
    If Length(password) < MIN_LENGTH Or Length(password) > MAX_LENGTH
        Return false
    End if
    number_of_lower ← 0
    number_of_upper ← 0
    number_of_digit ← 0
    number_of_special ← 0
    For each character in password
        If character is lowercase
            number_of_lower ← number_of_lower + 1
        End if
        If character is uppercase
            number_of_upper ← number_of_upper + 1
        End if
        If character is digit
            number_of_digit ← number_of_digit + 1
        End if
        If character in SPECIAL_CHARACTERS
            number_of_special ← number_of_special + 1
        End if
    End for
    If number_of_lower = 0 Or number_of_upper = 0 Or number_of_digit = 0
        Return false
    End if
    If IS_SPECIAL_CHARACTER_REQUIRED And number_of_special = 0
        Return false
    End if
    Return true
End function

Call main
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")

    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""

    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:

        if character.islower():
            number_of_lower += 1
        if character.isupper():
            number_of_upper += 1
        if character.isdigit():
            number_of_digit += 1
        if character in SPECIAL_CHARACTERS:
            number_of_special += 1
        pass

    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    # and return False if it's zero
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False
    # if we get here (without returning False), then the password must be valid
    return True


main()
