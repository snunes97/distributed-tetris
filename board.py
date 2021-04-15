import threading
import random
import time

from piece import Piece

class Board():
    def __init__(self):

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

        self.PIECE_I = [[0,0],[1,0],[2,0],[3,0]]
        self.PIECE_O = [[0,0],[0,1],[1,0],[1,1]]
        self.PIECE_T = [[0,1],[1,0],[1,1],[1,2]]
        self.PIECE_Z = [[0,1],[0,2],[1,0],[1,1]]
        self.PIECE_L = [[0,0],[0,1],[1,1],[1,2]]


        self.pieces = [self.PIECE_I, self.PIECE_O, self.PIECE_T, self.PIECE_Z, self.PIECE_L]

        self.active_piece = None

    def print_board(self):
        # print for testing
        for i in range(len(self.board)):
            print(self.board[i])

    def try_move_left(self):

        for pos in self.active_piece.shape_positions:
            if pos[1] <= 0:
                self.tick()
                return False

        self.draw_shape(0, self.active_piece)
        self.active_piece.move_left()
        self.tick()

    def try_move_right(self):

        for pos in self.active_piece.shape_positions:
            if pos[1] >= 10:
                self.tick()
                return False

        self.draw_shape(0, self.active_piece)
        self.active_piece.move_right()
        self.tick()

    def draw_shape(self, mode, shape):

        shape_pos = shape.shape_positions

        if mode == 1:
            for position in shape_pos:
                self.board[position[0]][position[1]] = mode

        if mode == 0:
            for position in shape_pos:
                self.board[position[0]][position[1]] = mode


    def place_new_piece(self):
        #pick random piece from piece list
        new_piece = Piece(random.choice(self.pieces))
        self.active_piece = new_piece
        self.draw_shape(1, self.active_piece)

        self.print_board()

    def tick(self):
        print("tick")
        self.draw_shape(0, self.active_piece)
        self.active_piece.move_down()
        self.draw_shape(1, self.active_piece)

        self.print_board()