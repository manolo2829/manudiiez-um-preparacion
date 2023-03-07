

class Buscaminas:


    def __init__(self, rows, columns, bombs):
        self.rows = rows
        self.columns = columns
        self.bombs = bombs
        self.board = []
        self.show = []

    def checkBoard(self):
        auxiliar = True
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                print(self.board[row][column], self.show[row][column])
                if self.board[row][column] == 'B' and self.show[row][column] != 'F':
                    auxiliar = False
        return auxiliar
    
    def win(self):
        return self.checkBoard()
    
    def lose(self):
        return not self.checkBoard()
    
    def question(self, movs):
        mov = input()
        row = input()
        col = input()

        if mov in movs and row <= self.rows and col <= self.columns:
            return mov, row, col
        else:
            raise Exception
        
    def play(self, mov, row, col):
        self.show[row][col] = 'F' if mov == 'flag' else self.board[row][col]
            