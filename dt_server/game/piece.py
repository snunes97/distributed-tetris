from copy import deepcopy

class Piece:
    def __init__(self, shape_up, shape_right, shape_down, shape_left):
        self.shape_up = shape_up
        self.shape_right = shape_right
        self.shape_down = shape_down
        self.shape_left = shape_left

        self.starting_shapes = [self.shape_up, self.shape_right, self.shape_down, self.shape_left]
        self.shapes = [deepcopy(self.shape_up), deepcopy(self.shape_right), deepcopy(self.shape_down), deepcopy(self.shape_left)]
        self.shape_index = 0

        self.downs = 0
        self.rights = 0

    def check_below(self, board):
        current_shape = self.current_shape()
        for i in range(len(current_shape)):
            if board[current_shape[i][0]+1][current_shape[i][1]] == 2:
                return True

    def check_left(self, board):
        current_shape = self.current_shape()
        for i in range(len(current_shape)):
            if board[current_shape[i][0]][current_shape[i][1]-1] == 2 or current_shape[i][1] <= 0:
                return True

    def check_right(self, board):
        current_shape = self.current_shape()
        for i in range(len(current_shape)):
            if current_shape[i][1] != 10:
                if board[current_shape[i][0]][current_shape[i][1]+1] == 2 or current_shape[i][1] >= 10:
                    return False
            else:
                return True

    def check_rotation_walls(self, board):
        blocked_positions = 0
        current_shape = self.current_shape()
        for i in range(len(current_shape)):
            if current_shape[i][1] == 10 or current_shape[i][1] == 0:
                blocked_positions += 1

        if blocked_positions >= 3:
            return False
        return True

    def check_rotation_pieces(self, rotated_shape, board):
        for i in range(len(rotated_shape)):
            print("ROTATED: " + str(board[rotated_shape[i][0]][rotated_shape[i][1]]))
            if board[rotated_shape[i][0]][rotated_shape[i][1]] == 2:
                print("OVERLAP!")
                return False
        return True

    def move_down(self):
        current_shape = self.current_shape()
        current_shape[0][0] += 1
        current_shape[1][0] += 1
        current_shape[2][0] += 1
        current_shape[3][0] += 1
        self.downs += 1

    def move_left(self):
        current_shape = self.current_shape()
        current_shape[0][1] -= 1
        current_shape[1][1] -= 1
        current_shape[2][1] -= 1
        current_shape[3][1] -= 1
        self.rights -= 1

    def move_right(self):
        current_shape = self.current_shape()
        current_shape[0][1] += 1
        current_shape[1][1] += 1
        current_shape[2][1] += 1
        current_shape[3][1] += 1
        self.rights += 1

    def rotate(self, board):
        self.shape_index = (self.shape_index + 1) % 4

        rotated_shape = deepcopy(self.shapes[self.shape_index])

        print("NEXT SHAPE ORIGINAL: " + str(rotated_shape))

        rotated_shape[0][0] += self.downs
        rotated_shape[1][0] += self.downs
        rotated_shape[2][0] += self.downs
        rotated_shape[3][0] += self.downs

        rotated_shape[0][1] += self.rights
        rotated_shape[1][1] += self.rights
        rotated_shape[2][1] += self.rights
        rotated_shape[3][1] += self.rights

        print("NEXT SHAPE W OFFSET: " + str(rotated_shape))

        if not self.check_rotation_pieces(rotated_shape, board):
            self.shape_index = (self.shape_index - 1) % 4
        else:
            self.shapes[(self.shape_index - 1) % 4] = self.starting_shapes[(self.shape_index - 1) % 4]

            # rotated_shape[0][0] -= 1
            # rotated_shape[1][0] -= 1
            # rotated_shape[2][0] -= 1
            # rotated_shape[3][0] -= 1

            self.shapes[self.shape_index] = rotated_shape

    def current_shape(self):
        return self.shapes[self.shape_index]