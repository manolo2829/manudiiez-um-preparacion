
class Letter:
    def __init__(self, letter='', positions=[]):
        self.letter = letter
        self.positions = positions

    def __repr__(self):
        return f"{self.letter}: {self.positions}"