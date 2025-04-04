# band.py
from musician import Musician
from guitar import Guitar


class Band:
    """A band that has a list of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def play(self):
        """Make all musicians play their instruments."""
        for musician in self.musicians:
            print(musician.play())


if __name__ == "__main__":
    # 测试代码
    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add_instrument(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add_instrument(Guitar("Takamine acoustic", 1986, 1200.00))
    gary = Musician("Gary Cherone")
    pat = Musician("Pat Badger")
    pat.add_instrument(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))
    kevin = Musician("Kevin Figueiredo")

    band.add_musician(nuno)
    band.add_musician(gary)
    band.add_musician(pat)
    band.add_musician(kevin)

    print("band (str)")
    print(band)
    print("band.play()")
    band.play()