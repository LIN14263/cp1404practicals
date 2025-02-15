"""
FILE_NAME <- "evil_capitalist.txt"
MAX_INCREASE <- 0.175
MAX_DECREASE <- 0.05
MIN_PRICE <- 1
MAX_PRICE <- 100
INITIAL_PRICE <- 10.0

price <- INITIAL_PRICE
Print formatted initial price with two decimal places
days <- 0

While MIN_PRICE <= price <= MAX_PRICE
    price_change <- 0
    random_num <- Randomly select an integer from 1 to 2
    If random_num = 1
        price_change <- Randomly select a floating - point number from 0 to MAX_INCREASE
    Else
        price_change <- Randomly select a floating - point number from - MAX_DECREASE to 0
    End If
    price <- price * (1 + price_change)
    days <- days + 1
    Print formatted current day's price with two decimal places
    Open FILE_NAME in append mode
    Write formatted price to file and add new line
    Close file
End While
"""
import random

FILE_NAME = "evil_capitalist.txt"
MAX_INCREASE = 0.175  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print(f"${price:,.2f}")
days = 0
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    days += 1
    print(f"On day {days} price is ${price:,.2f}")
    with open(FILE_NAME, "a") as out_file:
        out_file.write(f"{price}\n")
