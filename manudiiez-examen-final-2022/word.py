from letter import Letter

class Word:

    def __init__(self, word):
        self.word = word
        self.lista = []

    def encode(self):
        auxiliar = []
        position = 0
        for each in self.word:
            position += 1
            if each not in auxiliar:
                self.lista.append(Letter(each, [position]))
                auxiliar.append(each)
            else:
                for letter in self.lista:
                    if(letter.letter == each):
                        letter.positions.append(position)

        return self.lista
    
    def decode(self):
        auxiliar = []
        for each in self.word:
            for position in each.positions:
                auxiliar.append(position)
        for each in self.word:
            for position in each.positions:
                auxiliar[position-1] = each.letter

        return "".join(auxiliar)
