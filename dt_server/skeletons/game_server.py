import zmq
import game as game


class GameServer:
    def __init__(self, host: str, port_reqrep: int, port_pubsub: int, server: game.GameServer) -> None:
        self.port_reqrep = port_reqrep
        self.port_pubsub = port_pubsub
        self.host = host
        self.server = server

        context = zmq.Context()
        print("Opening game server...")
        self.conn_repreq = context.socket(zmq.REP)
        self.conn_repreq.bind("tcp://" + self.host + ":" + str(self.port_reqrep))
        print("REQREP connection successful!")

        self.conn_pubsub = context.socket(zmq.PUB)
        self.conn_pubsub.bind("tcp://" + self.host + ":" + str(self.port_pubsub))
        print("PUBSUB connection successful!")

    def validate_player(self):
        player_name = self.conn_repreq.recv_string()
        response = self.server.validate_player(player_name)
        self.conn_repreq.send_string(str(response))

    def dispatch_request(self, command):
        if command == game.OP_VALIDATEPLAYER:
            print("OP: VALIDATEPLAYER")
            self.conn_repreq.send_string("ACK")
            self.validate_player()

        if command == game.OP_MOVERIGHT:
            print("OP: MOVERIGHT")
            self.conn_repreq.send_string("ACK")
            self.server.move_right()

        if command == game.OP_MOVELEFT:
            print("OP: MOVELEFT")
            self.conn_repreq.send_string("ACK")
            self.server.move_left()

        if command == game.OP_ROT_R:
            print("OP: ROTRIGHT")
            self.conn_repreq.send_string("ACK")
            self.server.rotate_right()

        if command == game.OP_ROT_L:
            print("OP: ROTLEFT")
            self.conn_repreq.send_string("ACK")
            self.server.rotate_left()

        if command == game.OP_GETBOARD:
            print("OP: GETBOARD")
            board = self.server.get_board()
            board_string = self.board_to_string(board)
            self.conn_repreq.send_string(board_string)

    def board_to_string(self, board):
        board_string = ""
        line_start = True
        for line in board:
            for element in line:
                if line_start:
                    line_start = False
                    board_string += str(element)
                else:
                    board_string += "," + str(element)
            board_string += ";"
            line_start = True
        return board_string

    def run(self):
        print("Running...")
        while True:
            message = self.conn_repreq.recv_string()
            self.dispatch_request(message)
