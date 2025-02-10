"""
while sales > 0
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
LOWER_BONUS = 0.1
HIGHER_BONUS = 0.15
get sales
    if sales >= 1000
        bonus = sales * HIGHER_BONUS
        print(bonus)
        sales = float(input("Enter sales: $"))
    elif sales >= 0 and sales < 1000
        bonus = sales * LOWER_BONUS
        print(bonus)
        sales = float(input("Enter sales: $"))
print("The end")

"""
bonus = 0
LOWER_BONUS = 0.1
HIGHER_BONUS = 0.15
sales = float(input("Enter sales: $"))
while sales > 0:
    if sales >= 1000:
        bonus = sales * HIGHER_BONUS
    elif sales >= 0 and sales < 1000:
        bonus = sales * LOWER_BONUS
    print(bonus)
    sales = float(input("Enter sales: $"))
print("The end")