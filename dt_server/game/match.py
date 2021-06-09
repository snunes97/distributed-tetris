import random
import threading
import copy
from game.piece import Piece


class Match:
    def __init__(self, server):
        self.player_list = []
        self.server = server
        self.game_over = False

        self.TICK_RATE = 1

        # Defines the board
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

        # Defines the pieces
        # 3 Pieces (T and L - right and left /)

        # L piece and positions
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

        self.timer_on = False

    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def get_board(self):
        return self.board

    # Confirma se a casa está ocupada e anda lateralmente (verificar redundancia)
    def try_move_left(self, player_name):

        player_piece = self.find_player(player_name).get_active_piece()

        if not player_piece.check_left(self.board):
            self.draw_shape(0, player_piece, self.board)
            player_piece.move_left()
            self.draw_shape(1, player_piece, self.board)
        else:
            return False

    def try_move_right(self, player_name):

        player_piece = self.find_player(player_name).get_active_piece()

        if not player_piece.check_right(self.board):
            self.draw_shape(0, player_piece, self.board)
            player_piece.move_right()
            self.draw_shape(1, player_piece, self.board)
        else:
            return False

    def try_rotate(self, right, player_name):

        player_piece = self.find_player(player_name).get_active_piece()

        if player_piece.check_rotation_walls(self.board):
            self.draw_shape(0, player_piece, self.board)
            player_piece.rotate(self.board, right)
            self.draw_shape(1, player_piece, self.board)
        else:
            return False

    def draw_shape(self, mode, shape, board):
        # 0-Casa Vazia
        # 1-Peca Ativa
        # 2-Peca Colocada
        shape_pos = shape.current_shape()
        for position in shape_pos:
            board[position[0]][position[1]] = mode

    def clear_pieces(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    board[i][j] = 0
        return board

    def place_new_piece(self):

        for player in self.player_list:
            player_piece = player.get_active_piece()
            if player_piece is None:
                new_piece = copy.deepcopy(random.choice(self.pieces))
                player_piece = new_piece
                player_piece.piece_offset()

                # Confirma se a nova peça não se instancia em cima de uma peça trancada (o que é game over)
                for pos in player_piece.current_shape():
                    if self.board[pos[0]][pos[1]] == 2:
                        print("GG1")
                        # TODO: check quem é que ganhou/perdeu
                        self.set_game_over()
                        break
                if not self.game_over:
                    self.draw_shape(1, player_piece, self.board)
                else:
                    self.draw_shape(2, player_piece, self.board)

            player.set_active_piece(player_piece)

    def check_line(self, player):
        for line in self.board:
            if 0 not in line:
                self.board.remove(line)
                self.board.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                player.add_score(1)
                self.format_and_send_scores()

    def start_timer(self):
        threading.Timer(self.TICK_RATE, self.tick, [1]).start()

    def tick(self, timed):
        for pos in self.board[0]:
            if pos == 2:
                print("GG2")
                if not self.game_over:
                    # TODO: ver quem é que ganha/perde
                    self.set_game_over()
                    break

        if not self.game_over:

            for player in self.player_list:

                player_piece = player.get_active_piece()

                if player_piece is not None:

                    self.draw_shape(0, player_piece, self.board)
                    player_piece.move_down()
                    self.draw_shape(1, player_piece, self.board)

                    done_checking = False

                    # Confirma se a peça chegou ao fundo e marca-a como trancada
                    for pos in player_piece.current_shape():
                        print(str(player_piece.current_shape()))
                        if pos[0] >= 20:
                            done_checking = True
                            self.lock_piece(player, player_piece)
                            break

                    if not done_checking:
                        # Confirma se tem peça trancada por baixo
                        if player_piece.check_below(self.board):
                            # for pos in player_piece.current_shape():
                            #     if pos[0] == 20:
                            #         break
                            self.lock_piece(player, player_piece)

            if timed:
                self.start_timer()

            print("/////////////////////////////////////////////////////////")
            self.print_board()
            if not self.game_over:
                self.prepare_to_send_board(self.board, self.player_list)

    def lock_piece(self, player, player_piece):
        self.draw_shape(2, player_piece, self.board)
        self.check_line(player)
        player.set_active_piece(None)
        self.place_new_piece()

    def set_game_over(self):
        print("GAME OVER")
        self.game_over = True
        self.server.send_game_over()
        self.format_and_send_scores()

    def add_player(self, new_player):
        print(new_player.name + " JOINED THE MATCH")
        self.player_list.append(new_player)
        self.place_new_piece()
        if len(self.player_list) - 1 == 0:
            print("STARTING MATCH")
            self.print_board()
            print("////////////////////////////////////////////////FIRSTPRINT")
            self.start_timer()

    def player_name_is_unique(self, player_name):
        for player in self.player_list:
            if player_name == player.name:
                return False
        return True

    def find_player(self, player_name):
        for player in self.player_list:
            if player.name == player_name:
                return player

    def remove_player(self, player_name):
        for player in self.player_list:
            if player.name == player_name:
                player_piece = self.find_player(player_name).get_active_piece()
                self.draw_shape(0, player_piece, self.board)
                print(player_name + " LEFT THE MATCH")
                self.player_list.remove(player)

    def format_and_send_scores(self):
        scores_string = ""
        for player in self.player_list:
            scores_string += player.name + ":" + str(player.get_score()) + " | "
        self.server.send_scores(scores_string)

    def prepare_to_send_board(self, board, players):

        for player in players:
            temp_board = copy.deepcopy(board)
            player_board = self.draw_specific_player(temp_board, player.active_piece)
            self.server.send_board_update(player_board, player.name)

    def draw_specific_player(self, board, player_piece):
        if player_piece is not None:
            new_board = self.clear_pieces(board)
            self.draw_shape(1, player_piece, new_board)
            return new_board
        else:
            new_board = self.clear_pieces(board)
            return new_board
