import threading
from gui import Gui
from board import Board
from timer import Timer

gui = Gui()
board = Board(gui)

gui.start_gui()
board.place_new_piece()
board.print_board()

# # Código para mover automáticamente para baixo
# threading.Timer(1.0, board.tick).start()

stopFlag = threading.Event()
thread = Timer(stopFlag, board)
thread.start()

# this will stop the timer
# stopFlag.set()

while True:
    player_input = input("(asd): ")

    if player_input == "a":
        board.try_move_left()

    if player_input == "d":
        board.try_move_right()

    # Future features
    #
    # if player_input == "q":
    #     board.try_rotate_left()
    #
    # if player_input == "e":
    #     board.try_rotate_right()

    board.tick()
