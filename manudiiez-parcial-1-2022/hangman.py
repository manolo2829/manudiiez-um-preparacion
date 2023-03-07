from letter import Letter
from invalidassignmentexception import InvalidAssignmentException

class Hangman:

    def __init__(self):
        self.word = []
        self.lifes = 5

    def set_word(self, word):
        for each in word.lower():
            self.word.append(Letter(each))
    
    def assign(self, letter):
        letter = letter.lower()
        auxiliar = False
        for each in self.word:
            if each.value == letter:
                auxiliar = True
        if auxiliar:
            for i in range(len(self.word)):
                if self.word[i].value == letter:
                    self.word[i].display = self.word[i].value
        else:
            self.lifes -= 1
            raise InvalidAssignmentException('No Válido')


    def show(self):
        result = f"Lifes: {self.lifes} - Word: "
        for letter in self.word:
            result += f"{letter.display} "

        return result
    
            
    def winner(self):
        auxiliar = True
        for letter in self.word:
            if not letter.value == letter.display:
                auxiliar = False

        return auxiliar
    

    def play(self):
        while self.lifes > 0 and not self.winner():
            print(self.show())
            letter = input()
            try:
                self.assign(letter)
            except InvalidAssignmentException as err:
                print(err.args[0])
        print(self.show())
        if(self.lifes == 0):
            print('Perdiste')
            return 'Perdiste'
        else:
            print('Ganaste')
            return 'Ganaste'