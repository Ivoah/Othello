# TODO: Comments

import dataclasses

BLACK = '●'
WHITE = '○'

@dataclasses.dataclass(frozen=True)
class v2:
    r: int
    c: int

    def within(self, rs, cs):
        return rs[0] <= self.r <= rs[1] and cs[0] <= self.c <= cs[1]

    def __str__(self):
        return f'{chr(ord("A") + self.c)}{8 - self.r}'

    def __add__(self, other):
        return v2(
            self.r + other.r,
            self.c + other.c)

    def __sub__(self, other):
        return v2(
            self.r + other.r,
            self.c + other.c)

v2.NW = v2(-1, -1)
v2.N  = v2(-1,  0)
v2.NE = v2(-1,  1)
v2.W  = v2( 0, -1)
v2.E  = v2( 0,  1)
v2.SW = v2( 1, -1)
v2.S  = v2( 1,  0)
v2.SE = v2( 1,  1)

COMPASS = [v2.NW, v2.N, v2.NE, v2.W, v2.E, v2.SW, v2.S, v2.SE]
ALL_CELLS = [v2(r, c) for r in range(8) for c in range(8)]

class Board:
    def __init__(self):
        self.board = [[' ']*8 for _ in range(8)]
        self.board[3][3:5] = [BLACK, WHITE]
        self.board[4][3:5] = [WHITE, BLACK]

    def __getitem__(self, pos):
        return self.board[pos.r][pos.c]

    def __setitem__(self, pos, color):
        self.board[pos.r][pos.c] = color

    def _straight_line(self, pos, dir):
        if not (pos + dir).within((0, 7), (0, 7)) or self[pos] == ' ':
            return []
        elif not (pos + dir).within((0, 7), (0, 7)) or self[pos] != self[pos + dir]:
            return [pos]
        else:
            return [pos] + self._straight_line(pos + dir, dir)

    def copy(self):
        new_board = Board()
        new_board.board = [[self[v2(r, c)] for c in range(8)] for r in range(8)]
        return new_board

    def validMoves(self, color):
        moves = set()
        for pos in ALL_CELLS:
            if self[pos] == ' ':
                for dir in COMPASS:
                    line = self._straight_line(pos + dir, dir)
                    if line and self[line[-1]] != color and self[line[-1] + dir] == color:
                        moves.add(pos)
        return moves

    def makeMove(self, pos, color):
        self[pos] = color
        for dir in COMPASS:
            line = self._straight_line(pos + dir, dir)
            if line and self[line[-1] + dir] == color:
                for p in line: self[p] = color

    def score(self, color):
        return sum(self[pos] == color for pos in ALL_CELLS)

    def printBoard(self):
        print('    A   B   C   D   E   F   G   H')
        print('  ┌───┬───┬───┬───┬───┬───┬───┬───┐')
        print('  ├───┼───┼───┼───┼───┼───┼───┼───┤\n'.join(
            f'{8 - r} │ ' + ' │ '.join(self.board[r]) + ' │\n'
            for r in range(8)
        ), end='')
        print('  └───┴───┴───┴───┴───┴───┴───┴───┘')
        print(f'{BLACK}: {self.score(BLACK)}, {WHITE}: {self.score(WHITE)}')

    def printMoves(self, color):
        moves = self.validMoves(color)
        for move in moves: self[move] = '?'
        self.printBoard()
        for move in moves: self[move] = ' '
