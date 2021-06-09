import skeletons
import zmq
import game as game
import time
import threading

class ServerSkeleton:
    def __init__(self, host: str, port_reqrep: int, port_pubsub: int, server: game.Server) -> None:
        self.port_reqrep = port_reqrep
        self.port_pubsub = port_pubsub
        self.host = host
        self.server = server
        self.pubsub_topic_board = "boardupdate"
        self.pubsub_topic_score = "score"
        self.pubsub_topic_game = "game"

        context = zmq.Context()
        print("Opening game server...")

        self.conn_repreq = context.socket(zmq.REP)
        self.conn_repreq.bind("tcp://" + self.host + ":" + str(self.port_reqrep))
        print("REQREP connection successful!")

        self.conn_pubsub = context.socket(zmq.PUB)
        self.conn_pubsub.bind("tcp://" + self.host + ":" + str(self.port_pubsub))
        print("PUBSUB connection successful!")

        # threading.Thread(target=self.publish_board_update).start()

    # def publish_board_update(self):
    #     while True:
    #         if self.server.match_exists():
    #             message = self.server.get_board()
    #             self.conn_pubsub.send_string(str(self.pubsub_topic) + " " + self.board_to_string(message))
    #             time.sleep(1)
    #         else:
    #             time.sleep(1)

    def send_board_update(self, board, player_name):
        if self.server.match_exists():
            self.conn_pubsub.send_string(str(self.pubsub_topic_board) + player_name + "$" + self.board_to_string(board))

    def send_scores(self, scores):
        self.conn_pubsub.send_string(str(self.pubsub_topic_score) + "$" + scores)

    def send_game_over(self):
        self.conn_pubsub.send_string(str(self.pubsub_topic_game) + "$GAMEOVER")

    def validate_player(self):
        player_name = self.conn_repreq.recv_string()
        response = self.server.validate_player(player_name)
        self.conn_repreq.send_string(str(response))

    def dispatch_request(self, command):

        op, player_name = command.split("$")

        if op == skeletons.OP_VALIDATEPLAYER:
            print("OP: VALIDATEPLAYER")
            self.conn_repreq.send_string("ACK")
            self.validate_player()

        if op == skeletons.OP_MOVERIGHT:
            print("OP: MOVERIGHT")
            self.server.move_right(player_name)
            # self.send_board()

        if op == skeletons.OP_MOVELEFT:
            print("OP: MOVELEFT")
            self.server.move_left(player_name)
            # self.send_board()

        if op == skeletons.OP_ROT_R:
            print("OP: ROTRIGHT")
            self.server.rotate_right(player_name)
            # self.send_board()

        if op == skeletons.OP_ROT_L:
            print("OP: ROTLEFT")
            self.server.rotate_left(player_name)
            # self.send_board()

        if op == skeletons.OP_DISCONNECT:
            print("OP: DISCONNECT")
            self.server.disconnect(player_name)
            self.conn_repreq.send_string("BYE")

        if op == skeletons.OP_GETBOARD:
            print("OP: GETBOARD")
            self.send_board()

    def send_board(self):
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
