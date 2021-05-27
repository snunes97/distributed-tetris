import zmq
import stubs


class GameServer:
    def __init__(self, host: str, port_reqrep: int, port_pubsub: int) -> None:
        self.host = host
        self.port_reqrep = port_reqrep
        self.port_pubsub = port_pubsub

        context = zmq.Context()

        print("REPREQ: Connecting to game server")
        self.conn_reqrep = context.socket(zmq.REQ)
        self.conn_reqrep.connect("tcp://" + self.host + ":" + str(self.port_reqrep))

        print("PUBSUB: Connecting to game server")
        self.conn_pubsub = context.socket(zmq.SUB)
        self.conn_pubsub.connect("tcp://" + self.host + ":" + str(self.port_pubsub))

        print("Connected!")

    def validate_player(self, name: str):
        self.conn_reqrep.send_string(stubs.OP_VALIDATEPLAYER)
        print(self.conn_reqrep.recv_string())
        self.conn_reqrep.send_string(name)
        response = self.conn_reqrep.recv_string()
        return response

    def move_right(self):
        self.conn_reqrep.send_string(stubs.OP_MOVERIGHT)
        print(self.conn_reqrep.recv_string())

    def move_left(self):
        self.conn_reqrep.send_string(stubs.OP_MOVELEFT)
        print(self.conn_reqrep.recv_string())

    def rotate_right(self):
        self.conn_reqrep.send_string(stubs.OP_ROT_R)
        print(self.conn_reqrep.recv_string())

    def rotate_left(self):
        self.conn_reqrep.send_string(stubs.OP_ROT_L)
        print(self.conn_reqrep.recv_string())

    def get_board(self):
        self.conn_reqrep.send_string(stubs.OP_GETBOARD)
        return self.conn_reqrep.recv_string()
