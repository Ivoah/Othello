import random

class Random:
    def __init__(self, color):
        self.color = color

    def getMove(self, board):
        board.printBoard()
        return random.choice(list(board.validMoves(self.color)))

class MiniMax:
    def __init__(self, difficulty):
        self.difficulty = difficulty
    
    def __call__(self, color):
        self.color = color
        return self

    def getMove(self, board):
        board.printBoard()
        v = float('-inf')
        maxMoves = []
        for move in board.validMoves(self.color):
            new_board = board.copy()
            new_board.makeMove(move, self.color)
            m = self.min(new_board, self.difficulty)
            if v == m: maxMoves.append(move)
            elif v < m:
                maxMoves.clear()
                maxMoves.append(move)
        return random.choice(maxMoves)

    def min(self, board, depth):
        if depth == 0: return board.score(self.color)
        v = float('inf')
        for move in board.validMoves(self.color):
            new_board = board.copy()
            new_board.makeMove(move, self.color)
            v = min(v, self.max(new_board, depth - 1))
        return v

    def max(self, board, depth):
        if depth == 0: return board.score(self.color)
        v = float('-inf')
        for move in board.validMoves(self.color):
            new_board = board.copy()
            new_board.makeMove(move, self.color)
            v = max(v, self.min(new_board, depth - 1))
        return v
