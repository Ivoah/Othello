from Board import Board, BLACK, WHITE
from Human import Human
from AI import Random, MiniMax

class Othello:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = {
            BLACK: player1(BLACK),
            WHITE: player2(WHITE)
        }

    def play(self, turn=BLACK):
        while self.board.validMoves(turn):
            move = self.players[turn].getMove(self.board)
            self.board.makeMove(move, turn)
            turn = WHITE if turn == BLACK else BLACK
        print('Game over!')
        self.board.printBoard()
        if self.board.score(BLACK) > self.board.score(WHITE):
            print('Black wins!')
        elif self.board.score(WHITE) > self.board.score(BLACK):
            print('White wins!')
        else:
            print('It\'s a tie!')

if __name__ == '__main__':
    game = Othello(MiniMax(3), Random)
    game.play()
