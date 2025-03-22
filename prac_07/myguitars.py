# File: myguitars.py
from guitar import Guitar

def load_guitars(filename):
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    continue
                name, year, cost = parts
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def add_guitars(guitars):
    print("\nEnter new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = input("Year: ").strip()
        cost = input("Cost: ").strip()
        try:
            guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please try again.")
    return guitars

def save_guitars(guitars, filename):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("Guitars loaded:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    guitars = add_guitars(guitars)
    save_guitars(guitars, filename)
    print(f"\nUpdated guitars list saved to {filename}")


if __name__ == '__main__':
    main()