import zmq
import stubs


class GameServer:
    def __init__(self, host: str, port: int) -> None:
        self.port = port
        self.host = host

        context = zmq.Context()
        print("Connecting to game server")
        self.conn = context.socket(zmq.REQ)
        self.conn.connect("tcp://" + self.host + ":" + str(self.port))
        print("Connected!")

    def validate_player(self, name: str):
        self.conn.send_string(stubs.OP_VALIDATEPLAYER)
        response = self.conn.recv_string()
        print(response)
        self.conn.send_string(name)
        response = self.conn.recv_string()
        print(response)
        if response == "False":
            print("Player name already in use")
            self.try_enter()
        else:
            self.enter_game()

    def try_enter(self):
        newName = input("Insert your player name: ")
        self.validate_player(newName)

    def enter_game(self):
        print("Entering game...")