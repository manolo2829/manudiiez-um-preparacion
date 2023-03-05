from word import Word

class Phrase:
    def __init__(self):
        self.encoded = []
        self.decoded = []

    def __repr__(self):
        return f"{self.encoded}"
 
    def encode(self, phrase):
        for each in phrase.split(' '):
            word = Word(each)
            self.encoded.append(word.encode())
    
    def decode(self, phrase):
        for each in phrase:
            word = Word(each)
            self.decoded.append(word.decode())
        self.decoded = ' '.join(self.decoded)