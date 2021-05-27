import time

from stubs.game_server import GameServer
from ui.gui import Gui
import threading
from multiprocessing import Queue
#from pynput import keyboard
from pynput.keyboard import Listener


class Client():
    def __init__(self, server):
        self.BOARD_UPDATE_RATE = 1
        self.server = server
        self.queue = Queue
        self.name = ""

    def request_board_update(self):
        while True:
            self.print_board(self.format_board(self.server.get_board_update()))
            time.sleep(1)

    def try_enter(self):
        new_name = input("Insert your player name: ")
        is_validated = self.server.validate_player(new_name)

        if is_validated == "True":
            self.name = new_name
            self.enter_game()
            threading.Timer(self.BOARD_UPDATE_RATE, self.request_board_update).start()
        else:
            print("Player name already in use")
            self.try_enter()

    def enter_game(self):
        print("Entering game...")
        # gui = Gui(self.queue)
        # gui.start_gui()
        self.print_board(self.format_board(self.server.get_board()))
        input_listener = threading.Thread(target=self.start_input_listener)
        input_listener.start()

    def start_input_listener(self):
        while True:
            self.send_command()

    def on_press(self, key):
        print("Key pressed: {0}".format(key))
        if key.char == "a":
            self.print_board(self.format_board(self.server.move_left()))
        elif key.char == "d":
            self.print_board(self.format_board(self.server.move_right()))
        elif key.char == "e":
            self.print_board(self.format_board(self.server.rotate_right()))
        elif key.char == "q":
            self.print_board(self.format_board(self.server.rotate_left()))

    def send_command(self):
        with Listener(on_press=self.on_press) as listener:  # Create an instance of Listener
            listener.join()  # Join the listener thread to the main thread to keep waiting for keys

    def format_board(self, board_string):
        formatted_board = []
        rows = board_string.split(";")
        for row in rows:
            # elements = row.split(",")
            formatted_board.append(row)
        return formatted_board

    def print_board(self, board):
        # print for testing
        for i in range(len(board)):
            print(board[i])
            print(board[i])

    def get_board(self):
        self.print_board(self.format_board(self.server.get_board()))