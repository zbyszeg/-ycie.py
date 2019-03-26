from effect import Effect


class Effect6(Effect):
    def __init__(self, x, y, dx, dy, a, b):
        super().__init__(x, y, dx, dy, a, b)

    def apply(self):
        for i in range(self.x, self.dx + 1):
            for j in range(self.y, self.dy + 1):
                self.board2.board[i][j] = self.board1.board[i][j]
