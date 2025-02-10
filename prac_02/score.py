"""
procedure main
    score = random integer in range 0 to 100
    result = determine_score(score)
    print "Your result is " + result
end procedure

function determine_score(score)
    if score < 0 or score > 100
        result = "Invalid score"
    else if score > 90
        result = "Excellent"
    else if score > 50
        result = "Passable"
    else
        result = "Bad"
    return result
end function

call main
"""
import random


def main():
    """main function"""
    score = random.randint(0, 100)
    result = determine_score(score)
    print(f"Your result is {result}")


def determine_score(score):
    """determine what level the inputted score is"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
