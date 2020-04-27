from Board import Board, BLACK, WHITE

class Othello:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = {
            BLACK: player1(BLACK),
            WHITE: player2(WHITE)
        }

    def play(self, turn=BLACK, verbose=True):
        # Keep playing while there are still valid moves
        while self.board.validMoves(turn):
            if verbose: self.board.printMoves(turn)
            move = self.players[turn].getMove(self.board)
            self.board.makeMove(move, turn)
            turn = WHITE if turn == BLACK else BLACK
        if verbose:
            print('Game over!')
            self.board.printBoard()
            if self.board.score(BLACK) > self.board.score(WHITE):
                print('Black wins!')
            elif self.board.score(WHITE) > self.board.score(BLACK):
                print('White wins!')
            else:
                print('It\'s a tie!')

if __name__ == '__main__':
    import sys
    import time
    from Human import Human
    from AI import Random, MiniMax, AlphaBeta
    
    # Change Random to Human to play against AI
    game = Othello(AlphaBeta(3), Random)
    t0 = time.time()
    game.play(verbose=True)
    duration = time.time() - t0
    print(f'{duration:.2f}', game.board.score(BLACK), game.board.score(WHITE), game.board.score(BLACK) > game.board.score(WHITE), file=sys.stderr)
