class piece():
    def __init__(self, name, characteristics):
        self.name = str(''.join(characteristics))
        self.size = characteristics[0] 
        self.shape = characteristics[1]
        self.concave = characteristics[2]
        self.color = characteristics[3] 

class board():
    def __init__(self, combinations):
        self.remaining_pieces = []
        for index in range(0, len(combinations)):
            self.remaining_pieces.append(piece(index+1, combinations[index]))
        self.board_positions = [[0 for i in range(4)] for j in range(4)]
        self.filled = []

    def placePiece(self, pieceName, position):
        x, y = position.split()
        currentPiece = None 
        for piece in self.remaining_pieces:
            if piece.name == pieceName:
                currentPiece = piece
        if currentPiece is None:
            return False
        if self.board_positions[int(x)][int(y)] == 0:
            self.board_positions[int(x)][int(y)] = currentPiece
            self.remaining_pieces.remove(currentPiece)
        else:
            return False
    
    def checkValidPiece(self, pieceName):
        currentPiece = None
        for piece in self.remaining_pieces:
            if piece.name == pieceName:
                currentPiece = piece
                return True
        if currentPiece is None:
            return False

    def checkValidBoardPosition(self, position):
        try:
            x, y = position.split()
            test = self.board_positions[int(x)][int(y)]
            if test != 0:
                return False
            return True
        except:
            return False

    def displayRemaining(self):
        for piece in self.remaining_pieces:
            print(piece.name)

    def displayBoard(self):
        
        for row in self.board_positions:
            for col in row:
                if col != 0:
                    spaces = ' ' * (22 - len(col.name))
                    print(col.name, spaces, end=' ')
                else:
                    print('0', '                     ', end = ' ')
            print(' ')

    def checkHorizontal(self):
        filled_horizontal = []
        for i in range(4):
            for j in range(4):
                if self.board_positions[i][j] != 0:
                    filled_horizontal.append([i, j])
            if len(filled_horizontal) == 4:
                self.filled.append(filled_horizontal)
            filled_horizontal = []
        return self.filled

    def checkVertical(self):
        filled_vert = []
        for i in range(4):
            for j in range(4):
                if self.board_positions[j][i] != 0:
                    filled_vert.append([j, i])
            if len(filled_vert) == 4:
                self.filled.append(filled_vert)
            filled_vert = []
        return self.filled
    
    def checkDiag(self):
        diagonal = []
        for i in range(4):
            if self.board_positions[i][i] != 0:
                diagonal.append([i, i])
            if len(diagonal) == 4:
                self.filled.append(diagonal)
        diagonal = []
        for i in range(4):
            if self.board_positions[i][3-i] != 0:
                diagonal.append([i, 3-i])
            if len(diagonal) == 4:
                self.filled.append(diagonal)
        return self.filled

    def checkProperties(self, row):
        sizes = []
        shapes = []
        colors = []
        concaves = []
        properties = [sizes, shapes, colors, concaves]
        for position in row:
            piece = self.board_positions[position[0]][position[1]]
            sizes.append(piece.size)
            shapes.append(piece.shape)
            concaves.append(piece.concave)
            colors.append(piece.color)
        for prop in properties:
            if len(set(prop)) == 1:
                return True
        return False
            
    def checkForWin(self):
        self.checkHorizontal()
        self.checkVertical()
        self.checkDiag()
        for four_pieces in self.filled:
            if self.checkProperties(four_pieces) == True:
                return four_pieces
        return False

def main():
    sizes = ['Tall', 'Short']
    shapes = ['Circle', 'Square']
    fills = ['Open', 'Closed']
    colors = ['Light', 'Dark']
    combinations = [[i, j, k, l] for i in sizes
                                 for j in shapes
                                 for k in fills
                                 for l in colors]
    
    board_test = board(combinations)
    checkWin = False

    while(checkWin is False):
        print('The remaining pieces are :')
        board_test.displayRemaining()
        print('')
        print('The board looks like this: ')
        board_test.displayBoard()
        print('')

        piece_name = input('Player one, choose a piece to give to player two: ')
        valid_piece = board_test.checkValidPiece(piece_name)
        while not valid_piece:
            piece_name = input('Player one, that piece was invalid, please enter a valid piece: ')
            valid_piece = board_test.checkValidPiece(piece_name)

        position = input('Player two, choose a position to put your piece: ')
        valid_position = board_test.checkValidBoardPosition(position)
        while not valid_position:
            position = input('Player two, that position was invalid, please enter a position in the correct form (e.g. 0 1)')
            valid_position = board_test.checkValidBoardPosition(position)
        board_test.placePiece(piece_name, position)
        checkWin = board_test.checkForWin()
        if checkWin != False: 
            print('Player two has won!')
            board_test.displayBoard()

        print('The remaining pieces are :')
        board_test.displayRemaining()
        print('')
        print('The board looks like this: ')
        board_test.displayBoard()
        print('')

        piece_name = input('Player two, choose a piece to give to player one: ')
        valid_piece = board_test.checkValidPiece(piece_name)
        while not valid_piece:
            piece_name = input('Player two, that piece was invalid, please enter a valid piece: ')
            valid_piece = board_test.checkValidPiece(piece_name)

        position = input('Player one, choose a position to put your piece: ')
        valid_position = board_test.checkValidBoardPosition(position)
        while not valid_position:
            position = input('Player one, that position was invalid, please enter a position in the correct form (e.g. 0 1)')
            valid_position = board_test.checkValidBoardPosition(position)
        board_test.placePiece(piece_name, position)
        checkWin = board_test.checkForWin()
        if checkWin != False: 
            print('Player one has won!')
            board_test.displayBoard()

if __name__ == '__main__':
    main()