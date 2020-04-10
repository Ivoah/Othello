from Board import v2

class Human:
    def __init__(self, color):
        self.color = color

    def getMove(self, board):
        moves = board.validMoves(self.color)
        for move in moves: board[move] = '?'
        board.printBoard()
        for move in moves: board[move] = ' '
        while True:
            move = input(f'{self.color} turn, enter move: ')
            move = v2(
                8 - int(move[1]),
                ord(move[0].lower()) - ord('a'))
            if move in moves: break
            print('Invalid move')
        return move
