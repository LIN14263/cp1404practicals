from guitar import Guitar

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("My guitars!")
name = input("Name:")
while name != "":
    year = int(input("Year:"))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    print(f"{guitar} added.")
    guitars.append(guitar)
    name = input("Name:")

print("\nThese are my guitars:")
for i, new_guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if new_guitar.is_vintage() else ""
    print(f"Guitar {i}: {new_guitar.name:>20} ({new_guitar.year}), worth ${new_guitar.cost:10,.2f}{vintage_string}")

