import time
from stubs.client_stub import ClientStub
from ui.gui import Gui
import threading
from pynput.keyboard import Listener


class Client:
    def __init__(self, server):
        self.BOARD_UPDATE_RATE = 1
        self.server = server
        self.name = ""
        self.lock = threading.Lock()
        self.in_game = False
        self.input_listener = threading.Thread(target=self.send_command)

    # Periodicamente obtem e imprime a board mais recente
    def request_board_update(self):
        while True:
            if self.in_game and self.server.has_board_updates():
                self.print_board(self.format_board(self.server.get_board_update()))
                time.sleep(self.BOARD_UPDATE_RATE)

    # Corre quando o cliente é iniciado
    # O cliente envia um nome inserido pelo user e esse nome é validado pelo servidor
    # Se o nome é válido, o cliente entre num match
    # Se não, volta a pedir um nome
    def try_enter(self):
        new_name = input("Insert your player name: ")
        is_validated = self.server.validate_player(new_name)

        if is_validated == "True":
            self.name = new_name
            self.enter_game()
        else:
            print("Player name already in use")
            self.try_enter()

    # Corre quando o cliente submete um nome válido
    # Inicia a thread que recebe os updates periodicos da board
    # Inicia a thread do listener do teclado
    def enter_game(self):
        # gui = Gui(self.queue)
        # gui.start_gui()
        print("Entering match...")
        self.in_game = True
        threading.Thread(target=self.request_board_update).start()
        self.input_listener.start()

    # Inicia o listener do teclado
    def send_command(self):
        # while True:
        with Listener(on_press=self.on_press) as listener:  # Create an instance of Listener
            listener.join()  # Join the listener thread to the main thread to keep waiting for keys

    # Corre quando o listener do teclado deteta uma tecla a ser pressionada
    # Determina o que cada tecla faz
    def on_press(self, key):
        if self.in_game:
            # print("Key pressed: {0}".format(key))
            if key.char == "a":
                self.print_board(self.format_board(self.server.move_left(self.name)))
            elif key.char == "d":
                self.print_board(self.format_board(self.server.move_right(self.name)))
            elif key.char == "e":
                self.print_board(self.format_board(self.server.rotate_right(self.name)))
            elif key.char == "q":
                self.print_board(self.format_board(self.server.rotate_left(self.name)))
            elif key.char == "x":
                self.server.disconnect(self.name)
                self.in_game = False



    # Recebe a board em formato de string e formata para um estilo mais visivel
    def format_board(self, board_string):
        formatted_board = []
        rows = board_string.split(";")
        for row in rows:
            formatted_board.append(row.replace(",", " "))
        return formatted_board

    # Imprime a board (já formatada) que recebe como parâmetro
    def print_board(self, board):
        with self.lock:
            print("///////////////////////////////////////////////////")
            for i in range(len(board)):
                print(board[i])

    # Envia um pedido ao server para obter a board mais recente, formata-la e imprimi-la
    def get_board(self):
        self.print_board(self.format_board(self.server.get_board(self.name)))

    # Processa a finalização do match a que o cliente se encontra conectado
    def set_game_over(self):
        # self.get_board()
        print("GAME OVER")
        self.in_game = False
