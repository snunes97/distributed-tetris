import zmq
import game as game


class GameServer:
    def __init__(self, host: str, port: int, server: game.GameServer) -> None:
        self.port = port
        self.host = host
        self.server = server

        context = zmq.Context()
        print("Opening game server...")
        self.conn = context.socket(zmq.REP)
        self.conn.bind("tcp://" + self.host + ":" + str(self.port))

    def validate_player(self):
        player_name = self.conn.recv_string()
        response = self.server.validate_player(player_name)
        self.conn.send_string(str(response))

    def dispatch_request(self, command):
        if command == game.OP_VALIDATEPLAYER:
            print("OP: VALIDATEPLAYER")
            self.conn.send_string("ACK")
            self.validate_player()

        if command == game.OP_MOVERIGHT:
            print("OP: MOVERIGHT")
            self.conn.send_string("ACK")
            self.server.move_right()

        if command == game.OP_MOVELEFT:
            print("OP: MOVELEFT")
            self.conn.send_string("ACK")
            self.server.move_left()

    def run(self):
        print("Running...")
        while True:
            message = self.conn.recv_string()
            self.dispatch_request(message)
