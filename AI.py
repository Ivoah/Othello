# TODO: Comments

import random

from Board import BLACK, WHITE

class Random:
    def __init__(self, color):
        self.color = color

    def getMove(self, board):
        return random.choice(list(board.validMoves(self.color)))

class MiniMax:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def __call__(self, color):
        self.color = color
        self.opponent = BLACK if color == WHITE else WHITE
        return self

    def getMove(self, board):
        v = float('-inf')
        maxMoves = []
        for move in board.validMoves(self.color):
            new_board = board.copy()
            new_board.makeMove(move, self.color)
            m = self.min(new_board, self.difficulty)
            if v == m: maxMoves.append(move)
            elif v < m:
                v = m
                maxMoves = [move]
        return random.choice(maxMoves)

    def min(self, board, depth):
        if depth == 0: return board.score(self.color)
        v = float('inf')
        for move in board.validMoves(self.opponent):
            new_board = board.copy()
            new_board.makeMove(move, self.opponent)
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

class AlphaBeta(MiniMax):
    def getMove(self, board):
        α, β = float('-inf'), float('+inf')
        value = float('-inf')
        maxMoves = []
        for move in board.validMoves(self.color):
            child = board.copy()
            child.makeMove(move, self.color)
            ab = self.alphabeta(child, self.difficulty, α, β, self.opponent)
            if value == ab: maxMoves.append(move)
            elif value < ab:
                value = ab
                maxMoves = [move]
            α = max(α, value)
            if α >= β:
                break # β cut-off
        return random.choice(maxMoves)

        # return self.alphabeta(board, self.difficulty, float('-inf'), float('+inf'), self.color)

    def alphabeta(self, board, depth, α, β, player):
        if depth == 0 or not board.validMoves(player):
            return board.score(player)
        if player == self.color:
            value = float('-inf')
            for move in board.validMoves(player):
                child = board.copy()
                child.makeMove(move, player)
                value = max(value, self.alphabeta(child, depth - 1, α, β, self.opponent))
                α = max(α, value)
                if α >= β:
                    break # β cut-off
            return value
        else:
            value = float('+inf')
            for move in board.validMoves(player):
                child = board.copy()
                child.makeMove(move, player)
                value = min(value, self.alphabeta(child, depth - 1, α, β, self.color))
                β = min(β, value)
                if α >= β:
                    break # α cut-off
            return value
