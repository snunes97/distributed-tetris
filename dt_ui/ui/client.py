from stubs.game_server import GameServer
from ui.gui import Gui
from multiprocessing import Queue


class Client():
    def __init__(self, server):
        self.server = server
        self.queue = Queue

    def try_enter(self):
        new_name = input("Insert your player name: ")
        is_validated = self.server.validate_player(new_name)

        if is_validated == "True":
            self.enter_game()
        else:
            print("Player name already in use")
            self.try_enter()

    def enter_game(self):
        print("Entering game...")
        # gui = Gui(self.queue)
        # gui.start_gui()
        while True:
            self.send_command()

    def send_command(self):
        command = input("::> ")

        if command == "a":
            self.server.move_left()
        elif command == "d":
            self.server.move_right()
