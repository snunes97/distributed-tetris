class Piece:
    def __init__(self, shape_positions):
        self.shape_positions = shape_positions

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