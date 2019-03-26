from effect import Effect


class Effect5(Effect):
    def __init__(self, x, y, dx, dy, a, b):
        super().__init__(x, y, dx, dy, a, b)

        self.B_temp = [None] * 16
        for i in range(16):
            self.B_temp[i] = [None] * 16

        for i in range(16):
            for j in range(16):
                self.B_temp[i][j] = b.board[i][j]

    def apply(self):
        for i in range(self.x, self.dx + 1):
            for j in range(self.y, self.dy + 1):
                self.board2.board[i][j] = self.board1.board[i][j] ^ self.B_temp[i][j]
