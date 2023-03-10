from buscaminas import Buscaminas



if __name__ == '__main__':
    caso1 = [['2', 'B', '2', ' ', '1', 'B', 'B', '1'],
                      ['3', 'B', '3', ' ', '1', '3', '3', '2'],
                      ['3', 'B', '3', ' ', ' ', '1', 'B', '1'],
                      ['4', 'B', '3', ' ', ' ', '1', '1', '1'],
                      ['B', 'B', '2', ' ', ' ', ' ', ' ', ' '],
                      ['2', '2', '1', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', '1', '1', '1', ' ', ' ', ' '],
                      [' ', ' ', '1', 'B', '1', ' ', ' ', ' ']]
    
    buscaminas = Buscaminas(8, 8, 10)
    buscaminas.board = caso1
    buscaminas.show = [['2', 'F', '2', ' ', '1', 'F', 'F', '1'],
                        ['3', 'F', '3', ' ', '1', '3', '3', '2'],
                        ['3', 'F', '3', ' ', ' ', '1', 'F', '1'],
                        ['4', 'F', '3', ' ', ' ', '1', '1', '1'],
                        ['F', 'F', '2', ' ', ' ', ' ', ' ', ' '],
                        ['2', '2', '1', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', '1', '1', '1', ' ', ' ', ' '],
                        [' ', ' ', '1', 'F', '1', ' ', ' ', ' ']]
    print(buscaminas.win())