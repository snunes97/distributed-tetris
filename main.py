import threading
from gui import Gui
from board import Board
from timer import Timer

stopFlag = threading.Event()

board = Board()
board.place_new_piece()

guiThread = Gui(stopFlag, board)
guiThread.start_gui()

timerThread = Timer(stopFlag, board, guiThread)
timerThread.start()

# this will stop the timer
# stopFlag.set()

while True:
    player_input = input("a|d: ")

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
