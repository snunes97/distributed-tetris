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
            if Server.match.player_name_is_unique(player_name):
                new_player = Player(player_name)
                Server.match.add_player(new_player)
                return True
            return False

    @staticmethod
    def end_match():
        Server.match = None

    @staticmethod
    def move_right(player_name):
        Server.match.try_move_right(player_name)

    @staticmethod
    def move_left(player_name):
        Server.match.try_move_left(player_name)

    @staticmethod
    def rotate_right(player_name):
        Server.match.try_rotate(1, player_name)

    @staticmethod
    def rotate_left(player_name):
        Server.match.try_rotate(0, player_name)

    @staticmethod
    def disconnect(player_name):
        Server.match.remove_player(player_name)

    @staticmethod
    def get_board():
        return Server.match.get_board()

    @staticmethod
    def match_exists():
        return Server.match is not None

    @staticmethod
    def publish_board_update(board, player_name):
        Server.skeleton.publish_board_update(board, player_name)

    @staticmethod
    def reply_board_update(board):
        Server.skeleton.reply_board_update(board)

    @staticmethod
    def set_skeleton(skeleton):
        Server.skeleton = skeleton

    @staticmethod
    def send_scores(scores):
        Server.skeleton.send_scores(scores)

    @staticmethod
    def send_game_over(winner):
        Server.skeleton.send_game_over(winner)