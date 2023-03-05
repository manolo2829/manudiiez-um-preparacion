class Encoder:
    

    def __init__(self):
        self.dict = {}
        self.text = ""

    def encode(self, text):
        position = 0
        for letter in text:
            position += 1
            if not letter in self.dict:
                self.dict[letter] = [position]
            else:
                self.dict[letter].append(position)
        return self.dict
    
    def decode(self, dict):
        lista = []
        for letter in dict:
            for position in dict[letter]:
                lista.append(position)
        lista2 = lista

        for letter in dict:
            for position in dict[letter]:
                lista2[position-1] = letter
        return "".join(lista2)