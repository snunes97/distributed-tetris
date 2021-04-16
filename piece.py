class Piece:
    def __init__(self, shape_positions):
        self.shape_positions = shape_positions

    def check_bellow(self, board):
        for i in range(len(self.shape_positions)):
            if board[self.shape_positions[i][0]+1][self.shape_positions[i][1]] == 2:
                return True
    #
    # def check_right(self):
    # def check_left(self):

    def move_down(self):
        self.shape_positions[0][0] += 1
        self.shape_positions[1][0] += 1
        self.shape_positions[2][0] += 1
        self.shape_positions[3][0] += 1

    def move_left(self):
        self.shape_positions[0][1] -= 1
        self.shape_positions[1][1] -= 1
        self.shape_positions[2][1] -= 1
        self.shape_positions[3][1] -= 1

    def move_right(self):
        self.shape_positions[0][1] += 1
        self.shape_positions[1][1] += 1
        self.shape_positions[2][1] += 1
        self.shape_positions[3][1] += 1