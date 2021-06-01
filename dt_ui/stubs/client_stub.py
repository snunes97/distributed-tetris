import stubs
import time
import zmq
import threading

class ClientStub:
    def __init__(self, host: str, port_reqrep: int, port_pubsub: int) -> None:
        self.client = None
        self.host = host
        self.port_reqrep = port_reqrep
        self.port_pubsub = port_pubsub
        self.latest_board = None

        context = zmq.Context()

        print("REPREQ: Connecting to game server")
        self.conn_reqrep = context.socket(zmq.REQ)
        self.conn_reqrep.connect("tcp://" + self.host + ":" + str(self.port_reqrep))

        print("PUBSUB: Connecting to game server")
        self.conn_pubsub = context.socket(zmq.SUB)
        self.conn_pubsub.connect("tcp://" + self.host + ":" + str(self.port_pubsub))

        print("Connected!")

        # Topicos tratados pelas comunicações PUBSUB
        self.topic_filter_board = "boardupdate"
        self.topic_filter_score = "score"
        self.topic_filter_game = "game"

        self.conn_pubsub.setsockopt_string(zmq.SUBSCRIBE, self.topic_filter_board)
        self.conn_pubsub.setsockopt_string(zmq.SUBSCRIBE, self.topic_filter_score)
        self.conn_pubsub.setsockopt_string(zmq.SUBSCRIBE, self.topic_filter_game)

        self.subscriber_thread = threading.Thread(target=self.get_published_update)
        self.subscriber_thread.start()

    # Recebe mensagens PUBSUB, vê o tópico e decide o que é feito com o conteúdo da mensagem
    def get_published_update(self):
        while True:
            message = self.conn_pubsub.recv_string()
            topic, content = message.split("$")
            if topic == self.topic_filter_board:
                self.update_latest_board(content)
            elif topic == self.topic_filter_score:
                self.update_score(content)
            elif topic == self.topic_filter_game:
                if content == "GAMEOVER":
                    self.client.set_game_over()

    def update_score(self, score):
        print(score)

    def update_latest_board(self, board):
        self.latest_board = board
        time.sleep(0.2)

    def get_board_update(self):
        if self.latest_board is not None:
            return self.latest_board

    def has_board_updates(self):
        return self.latest_board is not None

    def validate_player(self, name: str):
        self.conn_reqrep.send_string(stubs.OP_VALIDATEPLAYER + "$" + name)
        print(self.conn_reqrep.recv_string())
        self.conn_reqrep.send_string(name)
        response = self.conn_reqrep.recv_string()
        return response

    def move_right(self, player_name):
        self.conn_reqrep.send_string(stubs.OP_MOVERIGHT + "$" + player_name)
        return self.conn_reqrep.recv_string()

    def move_left(self, player_name):
        self.conn_reqrep.send_string(stubs.OP_MOVELEFT + "$" + player_name)
        return self.conn_reqrep.recv_string()

    def rotate_right(self, player_name):
        self.conn_reqrep.send_string(stubs.OP_ROT_R + "$" + player_name)
        return self.conn_reqrep.recv_string()

    def rotate_left(self, player_name):
        self.conn_reqrep.send_string(stubs.OP_ROT_L + "$" + player_name)
        return self.conn_reqrep.recv_string()

    def get_board(self, player_name):
        self.conn_reqrep.send_string(stubs.OP_GETBOARD + "$" + player_name)
        return self.conn_reqrep.recv_string()

    def set_client(self, client):
        self.client = client
