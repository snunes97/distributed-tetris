import threading
from gui import Gui
from board import Board

board = Board()
gui = Gui()

# gui.start_gui()
board.place_new_piece()

while True:
    player_input = input("(asd): ")

    if player_input == "a":
        board.try_move_left()

    if player_input == "d":
        board.try_move_right()

# t = threading.Timer(1.0, board.tick)
# t.start()