import random
import threading
import copy
from game.piece import Piece

class Match:
    def __init__(self, player1, server):
        self.player1 = player1
        self.server = server
        self.game_over = False

        self.TICK_RATE = 1

        # Defines the board
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

        #Defines the pieces
        #3 Pieces (T and L - right and left /)

        #L piece and positions
        self.PIECE_L_UP = [[0, 1], [1, 1], [2, 1], [2, 2]]
        self.PIECE_L_RIGHT = [[1, 0], [1, 1], [1, 2], [2, 0]]
        self.PIECE_L_DOWN = [[0, 0], [0, 1], [1, 1], [2, 1]]
        self.PIECE_L_LEFT = [[1, 0], [1, 1], [1, 2], [0, 2]]
        # J piece and positions
        self.PIECE_J_UP = [[0, 1], [1, 1], [2, 1], [2, 0]]
        self.PIECE_J_RIGHT = [[0, 0], [1, 0], [1, 1], [1, 2]]
        self.PIECE_J_DOWN = [[0, 1], [0, 2], [1, 1], [2, 1]]
        self.PIECE_J_LEFT = [[1, 0], [1, 1], [1, 2], [2, 2]]
        # T piece and positions
        self.PIECE_T_UP = [[1, 0], [1, 1], [1, 2], [0, 1]]
        self.PIECE_T_RIGHT = [[0, 1], [1, 1], [2, 1], [1, 2]]
        self.PIECE_T_DOWN = [[1, 0], [1, 1], [1, 2], [2, 1]]
        self.PIECE_T_LEFT = [[1, 0], [0, 1], [1, 1], [2, 1]]

        piece_l = Piece(self.PIECE_L_UP, self.PIECE_L_RIGHT, self.PIECE_L_DOWN, self.PIECE_L_LEFT)
        piece_j = Piece(self.PIECE_J_UP, self.PIECE_J_RIGHT, self.PIECE_J_DOWN, self.PIECE_J_LEFT)
        piece_t = Piece(self.PIECE_T_UP, self.PIECE_T_RIGHT, self.PIECE_T_DOWN, self.PIECE_T_LEFT)

        # self.PIECE_J = [[1, 0], [0, 0], [0, 1], [0, 2]]
        # self.PIECE_T = [[0, 1], [1, 0], [1, 1], [1, 2]]

        self.pieces = [piece_l, piece_j, piece_t]

        self.active_piece = None
        self.timer_on = False

    def print_board(self):
        # print for testing
        for i in range(len(self.board)):
            print(self.board[i])

    def get_board(self):
        return self.board

    #confirma se a casa está ocupada e anda lateralmente (verificar redundancia)
    def try_move_left(self):
        if not self.active_piece.check_left(self.board):
            self.draw_shape(0, self.active_piece)
            self.active_piece.move_left()
        else:
            return False

    def try_move_right(self):
        if not self.active_piece.check_right(self.board):
            self.draw_shape(0, self.active_piece)
            self.active_piece.move_right()
        else:
            return False

    def try_rotate(self, right):
        if self.active_piece.check_rotation_walls(self.board):
            self.draw_shape(0, self.active_piece)
            self.active_piece.rotate(self.board, right)
        else:
            return False

    def draw_shape(self, mode, shape):
        #0-Casa Vazia
        #1-Peca Ativa
        #2-Peca Colocada
        shape_pos = shape.current_shape()
        for position in shape_pos:
            self.board[position[0]][position[1]] = mode

    def place_new_piece(self):
        #pick random piece from piece list
        new_piece = copy.deepcopy(random.choice(self.pieces))
        self.active_piece = new_piece
        self.active_piece.piece_offset()
        for pos in self.active_piece.current_shape():
            if self.board[pos[0]][pos[1]] == 2:
                print("GG1")
                self.set_game_over()
                break
        if not self.game_over:
            self.draw_shape(1, self.active_piece)
        else:
            self.draw_shape(2, self.active_piece)

    def check_line(self):
        for line in self.board:
            if 0 not in line:
                self.board.remove(line)
                self.board.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                self.player1.add_score(1)
                self.server.send_scores(self.player1)
                print(self.player1.get_name() + ": " + str(self.player1.get_score()))

    def start_timer(self):
        threading.Timer(self.TICK_RATE, self.tick, [1]).start()

    def tick(self, timed):

        for pos in self.board[0]:
            if pos == 2:
                print("GG2")
                if not self.game_over:
                    self.set_game_over()
                    break

        if not self.game_over:

            self.draw_shape(0, self.active_piece)
            self.active_piece.move_down()
            self.draw_shape(1, self.active_piece)

            for pos in self.active_piece.current_shape():
                if pos[0] >= 20:
                    self.draw_shape(2, self.active_piece)
                    self.check_line()
                    self.place_new_piece()
                    break

            # #Confirma se não tem peça por baixo
            if self.active_piece.check_below(self.board):
                for pos in self.active_piece.current_shape():
                    if pos[0] == 0:
                        break

                self.draw_shape(2, self.active_piece)
                self.check_line()
                self.place_new_piece()

            if timed:
                self.start_timer()

            print("/////////////////////////////////////////////////////////")
            self.print_board()
            if not self.game_over:
                self.server.send_board_update(self.board)

    def set_game_over(self):
        print("GAME OVER")
        self.game_over = True
        self.server.send_game_over()
        self.server.send_scores(self.player1)