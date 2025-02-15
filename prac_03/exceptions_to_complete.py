"""
is_finished ← false
while is_finished = false
    try
        result ← prompt user "Enter a valid integer: " and convert input to integer
        is_finished ← true
    catch ValueError
        print "Please enter a valid integer."
    end try
end while
print "Valid result is:", result
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except  ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)  # no problem with undefined variable
