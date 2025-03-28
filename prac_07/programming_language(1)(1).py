class ProgrammingLanguage:
    """
    A class to represent a programming language.
    """

    def __init__(self, name, year, reflection, pointer_arithmetic):
        self.name = name
        self.year = year
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        return f"{self.name} (Created: {self.year}) | Reflection: {self.reflection} | Pointer Arithmetic: {self.pointer_arithmetic}"
