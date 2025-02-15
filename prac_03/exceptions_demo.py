"""
fraction ← False

While fraction = False
    Try
        numerator ← Prompt user "Enter the numerator: " and convert input to integer
        denominator ← Prompt user "Enter the denominator: " and convert input to integer
        fraction ← numerator / denominator
        Print fraction
        fraction ← True
    Catch ValueError
        Print "Numerator and denominator must be valid numbers!"
    Catch ZeroDivisionError
        Print "Cannot divide by zero!"
    End Try
End While

Print "Finished."
"""
fraction = False
while not fraction:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        fraction = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")
