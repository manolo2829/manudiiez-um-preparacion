from element import Element
from invalidAssignmentException import InvalidAssignmentException

class Hangman:

    def __init__(self):
        self.word = []
        self.lifes = 5

    def set_word(self, word):
        word = word.lower()
        for letter in word:
            self.word.append(Element(letter))

    def show(self):
        auxiliar = f"Lifes: {self.lifes} - Word: "
        for element in self.word:
            auxiliar += f"{element.display} "
        return auxiliar
    
    def assign(self, letter):
        letter = letter.lower()
        auxiliar = False
        for element in self.word:
            if element.letter == letter:
                auxiliar = True
                element.display = element.letter
        if not auxiliar:
            self.lifes -= 1
            raise InvalidAssignmentException('No valido')
        
    def winner(self):
        auxiliar = True
        for element in self.word:
            if element.letter != element.display:
                auxiliar = False
        return auxiliar
    
    def play(self):
        while self.lifes > 0 and not self.winner():
            print(self.show())
            letter = input()
            try:
                self.assign(letter)
            except InvalidAssignmentException as err:
                print(err)
            print(self.show())
        
        if self.lifes > 0:
            return 'Ganaste'
        else:
            return 'Perdiste'
