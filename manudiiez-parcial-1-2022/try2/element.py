

class Element:
    def __init__(self, letter='', display='_'):
        self.letter = letter
        self.display = display
    def __repr__(self):
        return f"letter: {self.letter} -- display: {self.display}"
    