from guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
expected_age_1 = 102
expected_vintage_1 = True

guitar_2 = Guitar("Another Guitar", 2013, 1000.00)
expected_age_2 = 11
expected_vintage_2 = False

print(f"{guitar_1.name} get_age() - Expected {expected_age_1}. Got {guitar_1.get_age()}")
print(f"{guitar_2.name} get_age() - Expected {expected_age_2}. Got {guitar_2.get_age()}")
print(f"{guitar_1.name} is_vintage() - Expected {expected_vintage_1}. Got {guitar_1.is_vintage()}")
print(f"{guitar_2.name} is_vintage() - Expected {expected_vintage_2}. Got {guitar_2.is_vintage()}")

