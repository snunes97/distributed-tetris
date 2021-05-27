import time

import zmq
import stubs
import threading

class GameServer:
    def __init__(self, host: str, port_reqrep: int, port_pubsub: int) -> None:
        self.host = host
        self.port_reqrep = port_reqrep
        self.port_pubsub = port_pubsub
        self.board_updates = []

        context = zmq.Context()

        print("REPREQ: Connecting to game server")
        self.conn_reqrep = context.socket(zmq.REQ)
        self.conn_reqrep.connect("tcp://" + self.host + ":" + str(self.port_reqrep))

        print("PUBSUB: Connecting to game server")
        self.conn_pubsub = context.socket(zmq.SUB)
        self.conn_pubsub.connect("tcp://" + self.host + ":" + str(self.port_pubsub))

        print("Connected!")

        topic_filter = "boardupdate"
        self.conn_pubsub.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

        threading.Thread(target=self.get_board_update_message).start()

    def get_board_update_message(self):
        while True:
            message = self.conn_pubsub.recv_string()
            topic, board = message.split()
            self.board_updates.append(board)
            time.sleep(1)

    def get_board_update(self):
        return self.board_updates.pop(0)

    def has_board_updates(self):
        return len(self.board_updates) > 0

    def validate_player(self, name: str):
        self.conn_reqrep.send_string(stubs.OP_VALIDATEPLAYER)
        print(self.conn_reqrep.recv_string())
        self.conn_reqrep.send_string(name)
        response = self.conn_reqrep.recv_string()
        return response

    def move_right(self):
        self.conn_reqrep.send_string(stubs.OP_MOVERIGHT)
        self.clear_board_updates()
        return self.conn_reqrep.recv_string()

    def move_left(self):
        self.conn_reqrep.send_string(stubs.OP_MOVELEFT)
        self.clear_board_updates()
        return self.conn_reqrep.recv_string()

    def rotate_right(self):
        self.conn_reqrep.send_string(stubs.OP_ROT_R)
        self.clear_board_updates()
        return self.conn_reqrep.recv_string()

    def rotate_left(self):
        self.conn_reqrep.send_string(stubs.OP_ROT_L)
        self.clear_board_updates()
        return self.conn_reqrep.recv_string()

    def get_board(self):
        self.conn_reqrep.send_string(stubs.OP_GETBOARD)
        return self.conn_reqrep.recv_string()

    def match_exists(self):
        self.conn_reqrep.send_string(stubs.OP_MATCHEXISTS)
        return self.conn_reqrep.recv_string()

    def clear_board_updates(self):
        self.board_updates = []