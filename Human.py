# TODO: Comments

from Board import v2

# Let a human play the game
class Human:
    def __init__(self, color):
        self.color = color

    def getMove(self, board):
        moves = board.validMoves(self.color)
        while True:
            move = input(f'{self.color} turn, enter move: ')
            move = v2(
                8 - int(move[1]),
                ord(move[0].lower()) - ord('a'))
            if move in moves: break
            print('Invalid move')
        return move
