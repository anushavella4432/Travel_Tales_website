class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

    def __str__(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

    def __eq__(self, other):
        if isinstance(other, Date):
            return (self.day, self.month, self.year) == (other.day, other.month, other.year)
        return False

    def __lt__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) < (other.year, other.month, other.day)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Date):
            return self < other or self == other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) > (other.year, other.month, other.day)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Date):
            return self > other or self == other
        return NotImplemented
