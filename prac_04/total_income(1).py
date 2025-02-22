"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_number = int(input("How many months? "))

    for month in range(1, month_number + 1):
        income = float(input(f"Enter income for month {month}:"))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print_report(incomes, month_number)


def print_report(incomes, month_number):
    """print calculated report"""
    total = 0
    for month in range(1, month_number + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
