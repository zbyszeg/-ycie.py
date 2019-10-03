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


class Effect0(Effect):
    def __init__(self, x, y, dx, dy, a, b):
        super().__init__(x, y, dx, dy, a, b)

    def apply(self):
        for i in range(self.x, self.dx + 1):
            for j in range(self.y, self.dy + 1):
                self.board1.board[i][j] = 0


class Effect1(Effect):
    def __init__(self, x, y, dx, dy, a, b):
        super().__init__(x, y, dx, dy, a, b)

    def apply(self):
        for i in range(self.x, self.dx + 1):
            for j in range(self.y, self.dy + 1):
                self.board1.board[i][j] = 1


class Effect2(Effect):
    def __init__(self, x, y, dx, dy, a, b):
        super().__init__(x, y, dx, dy, a, b)

    def apply(self):
        for i in range(self.x, self.dx + 1):
            for j in range(self.y, self.dy + 1):
                if self.board1.board[i][j] == 0:
                    self.board1.board[i][j] = 1
                else:
                    self.board1.board[i][j] = 0


class Effect3(Effect):
    def __init__(self, x, y, dx, dy, a, b):
        super().__init__(x, y, dx, dy, a, b)

    def apply(self):
        temp = [None] * 16
        for i in range(16):
            temp[i] = [None] * 16

        for i in range(16):
            for j in range(16):
                temp[i][j] = self.board1.board[i][j]

        for i in range(self.x, self.dx + 1):
            for j in range(self.y, self.dy + 1):
                if temp[i][j] == 1:
                    _sum = 0
                    for k in range(i - 1, i + 2):
                        temp_k = k
                        if k == -1:
                            k = 15
                        if k == 16:
                            k = 0
                        for l in range(j - 1, j + 2):
                            temp_l = l
                            if l == -1:
                                l = 15
                            if l == 16:
                                l = 0
                            _sum += temp[k][l]
                            l = temp_l
                        k = temp_k
                    _sum -= temp[i][j]
                    if (_sum != 2) and (_sum != 3):
                        self.board1.board[i][j] = 0
                    else:
                        self.board1.board[i][j] = 1
                else:
                    self.board1.board[i][j] = 0


class Effect4(Effect):
    def __init__(self, x, y, dx, dy, a, b):
        super().__init__(x, y, dx, dy, a, b)

    def apply(self):
        temp = [None] * 16
        for i in range(16):
            temp[i] = [None] * 16

        for i in range(16):
            for j in range(16):
                temp[i][j] = self.board1.board[i][j]

        for i in range(self.x, self.dx + 1):
            for j in range(self.y, self.dy + 1):
                if temp[i][j] == 0:
                    _sum = 0
                    for k in range(i - 1, i + 2):
                        temp_k = k
                        if k == -1:
                            k = 15
                        if k == 16:
                            k = 0
                        for l in range(j - 1, j + 2):
                            temp_l = l
                            if l == -1: l = 15
                            if l == 16: l = 0
                            _sum += temp[k][l]
                            l = temp_l
                        k = temp_k
                    if _sum == 3:
                        self.board1.board[i][j] = 1
                    else:
                        self.board1.board[i][j] = 0
                else:
                    self.board1.board[i][j] = 0


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


class Effect6(Effect):
    def __init__(self, x, y, dx, dy, a, b):
        super().__init__(x, y, dx, dy, a, b)

    def apply(self):
        for i in range(self.x, self.dx + 1):
            for j in range(self.y, self.dy + 1):
                self.board2.board[i][j] = self.board1.board[i][j]
