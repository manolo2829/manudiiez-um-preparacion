
class Compress:

    def __init__(self):
        self.compressed = []
        self.values = {}

    def compress(self, text):
        words = text.split(' ')
        position = 1
        for word in words:
            if not word in self.values:
                self.values[word] = position
                position = position+1
        for word in words:
            self.compressed.append(self.values[word])
        return self.compressed, self.values
    
    def uncompress(self, compressed, values):
        self.compressed = []

        for index in compressed:
            for word, position in values.items(): 
                if position == index:
                    self.compressed.append(word)
        return " ".join(self.compressed)