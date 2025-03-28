CURRENT_YEAR = 2022
VINTAGE_AGE = 50

# File: guitar.py
class Guitar:
    """
    Represents a guitar with a name, year, and cost.
    """
    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year
