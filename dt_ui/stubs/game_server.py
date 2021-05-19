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
        print(self.conn.recv_string())
        self.conn.send_string(name)
        response = self.conn.recv_string()
        return response

    def move_right(self):
        self.conn.send_string(stubs.OP_MOVERIGHT)
        print(self.conn.recv_string())

    def move_left(self):
        self.conn.send_string(stubs.OP_MOVELEFT)
        print(self.conn.recv_string())

    def rotate(self):
        self.conn.send_string(stubs.OP_ROT)
        print(self.conn.recv_string())