import threading
from gui import Gui
from board import Board

board = Board()
gui = Gui()

# gui.start_gui()
board.place_new_piece()
board.print_board()

while True:
    player_input = input("(asd): ")

    if player_input == "a":
        board.try_move_left()

    if player_input == "d":
        board.try_move_right()

    # Future features
    if player_input == "s":
        board.try_move_down()
    #
    # if player_input == "q":
    #     board.try_rotate_left()
    #
    # if player_input == "e":
    #     board.try_rotate_right()

    board.tick()