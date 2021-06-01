from game.player import Player
from game.match import Match


class Server:
    skeleton = None
    match = None

    @staticmethod
    def create_new_match():
        match1 = Match(Server)
        Server.match = match1

    @staticmethod
    def validate_player(player_name: str):

        if Server.match is None:
            Server.create_new_match()
            new_player = Player(player_name)
            Server.match.add_player(new_player)
            return True
        else:
            if not Server.match.player_name_is_duplicated(player_name):
                new_player = Player(player_name)
                Server.match.add_player(new_player)
                return True
            return False

    @staticmethod
    def move_right(player_name):
        Server.match.try_move_right(player_name)
        # Server.match.tick(0)

    @staticmethod
    def move_left(player_name):
        Server.match.try_move_left(player_name)
        # Server.match.tick(0)

    @staticmethod
    def rotate_right(player_name):
        Server.match.try_rotate(1, player_name)
        # Server.match.tick(0)

    @staticmethod
    def rotate_left(player_name):
        Server.match.try_rotate(0, player_name)
        # Server.match.tick(0)

    @staticmethod
    def get_board():
        return Server.match.get_board()

    @staticmethod
    def match_exists():
        return Server.match is not None

    @staticmethod
    def send_board_update(board):
        Server.skeleton.send_board_update(board)

    @staticmethod
    def set_skeleton(skeleton):
        Server.skeleton = skeleton

    @staticmethod
    def send_scores(scores):
        Server.skeleton.send_scores(scores)

    @staticmethod
    def send_game_over():
        Server.skeleton.send_game_over()