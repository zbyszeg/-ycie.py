class Board:
    def __init__(self):
        self.size = 16
        self.board = [0] * self.size
        for i in range(self.size):
            self.board[i] = [0] * self.size

    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end='')
            print()
