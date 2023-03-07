class inLine:

    def __init__(self):
        self.board = self.createBoard()
    
    def createBoard(self):
        lista = []
        for row in range(6):
            lista.append([])
            for column in range(7):
                lista[row].append(0)
        return lista