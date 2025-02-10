"""
Define the MENU options for:
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit

Display the MENU

Define main function:
    Prompt the user for input and store it in 'choice' (convert to uppercase)

    While 'choice' is not "Q":
        If 'choice' is "C":
            Prompt for Celsius input and convert it to a float
            Call calculate_fahrenheit with the Celsius value and store the result
            Display the Fahrenheit result rounded to two decimal places
        Else if 'choice' is "F":
            Prompt for Fahrenheit input and convert it to a float
            Call calculate_celsius with the Fahrenheit value and store the result
            Display the Celsius result rounded to two decimal places
        Else:
            Print "Invalid option"

        Display the MENU again
        Prompt for new 'choice' input (convert to uppercase)

    Print "Thank you."

Define function calculate_celsius(fahrenheit):
    Calculate Celsius from Fahrenheit using the formula: Celsius = (5 / 9) * (fahrenheit - 32)
    Return the Celsius value

Define function calculate_fahrenheit(celsius):
    Calculate Fahrenheit from Celsius using the formula: Fahrenheit = (celsius * 9.0 / 5) + 32
    Return the Fahrenheit value

Call the main function

"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


def main():
    """main function"""
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = calculate_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius(fahrenheit):
    """calculate from fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def calculate_fahrenheit(celsius):
    """calculate from celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()
