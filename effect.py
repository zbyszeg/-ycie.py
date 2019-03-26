from board import Board


class Effect:
    def __init__(self, x, y, dx, dy, a=Board(), b=Board()):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.board1 = a
        self.board2 = b

    def apply(self):
        pass
