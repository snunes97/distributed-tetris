import random
import copy
from piece import Piece

class Board():
    def __init__(self):

        #Defines the board
        self.board = [[0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0]]

        #Defines the pieces
            #7 Pieces
        self.PIECE_I = [[0, 0], [0, 1], [0, 2], [0, 3]]
        self.PIECE_O = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.PIECE_T = [[0, 1], [1, 0], [1, 1], [1, 2]]
        self.PIECE_Z = [[0, 0], [0, 1], [1, 1], [1, 2]]
        self.PIECE_N = [[1, 0], [1, 1], [0, 1], [0, 2]]
        self.PIECE_L = [[0, 0], [0, 1], [0, 2], [1, 2]]
        self.PIECE_J = [[1, 0], [0, 0], [0, 1], [0, 2]]

        self.pieces = [self.PIECE_I, self.PIECE_O, self.PIECE_T, self.PIECE_Z, self.PIECE_N, self.PIECE_J, self.PIECE_L]

            #7 Colors
        self.shape_colors = [(0, 255, 255), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

        self.active_piece = None
        self.timer_on = False


    def print_board(self):
        # print for testing
        for i in range(len(self.board)):
            print(self.board[i])

    #confirma se a casa está ocupada e anda lateralmente (verificar redundancia)
    def try_move_left(self):
        if self.active_piece.check_left(self.board) is True:
            for pos in self.active_piece.shape_positions:
                if pos[1] <= 0:
                    return False
        self.draw_shape(0, self.active_piece)
        self.active_piece.move_left()

    def try_move_right(self):
        if self.active_piece.check_right(self.board) is True:
            for pos in self.active_piece.shape_positions:
                if pos[1] >= 10:
                    return False
        self.draw_shape(0, self.active_piece)
        self.active_piece.move_right()

    def draw_shape(self, mode, shape):
        #0-Casa Vazia
        #1-Peca Ativa
        #2-Peca Colocada
        shape_pos = shape.shape_positions
        for position in shape_pos:
            self.board[position[0]][position[1]] = mode

    def place_new_piece(self):
        #pick random piece from piece list
        new_piece = Piece(copy.deepcopy(random.choice(self.pieces)))
        self.active_piece = new_piece
        self.draw_shape(1, self.active_piece)

    def check_line(self):
        for line in self.board:
            if 0 not in line:
                self.board.remove(line)
                self.board.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def tick(self):
        self.draw_shape(0, self.active_piece)
        self.active_piece.move_down()
        self.draw_shape(1, self.active_piece)

        for pos in self.active_piece.shape_positions:
            if pos[0] >= 20:
                self.draw_shape(2, self.active_piece)
                self.check_line()
                self.place_new_piece()
                break

        #Confirma se não tem peça por baixo
        if self.active_piece.check_bellow(self.board):
            for pos in self.active_piece.shape_positions:
                if pos[0] == 0:
                    break #endgame?

            self.draw_shape(2, self.active_piece)
            self.check_line()
            self.place_new_piece()


        print("/////////////////////////////////////////////////////////")
        self.print_board()