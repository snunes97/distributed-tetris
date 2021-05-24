from game.player import Player
from game.match import Match


class GameServer:
    match = None
    p_test = Player("coisa")
    player_list = [p_test]

    @staticmethod
    def start_new_match(player1):
        match1 = Match(player1)
        GameServer.match = match1
        GameServer.match.place_new_piece()
        GameServer.match.print_board()
        GameServer.match.start_timer()

    @staticmethod
    def validate_player(name: str):
        for player in GameServer.player_list:
            if name == player.name:
                return False

        new_player = Player(name)
        GameServer.player_list.append(new_player)
        GameServer.start_new_match(new_player)
        return True

    @staticmethod
    def move_right():
        GameServer.match.try_move_right()
        GameServer.match.tick(0)

    @staticmethod
    def move_left():
        GameServer.match.try_move_left()
        GameServer.match.tick(0)

    @staticmethod
    def rotate_right():
        GameServer.match.try_rotate(1)
        GameServer.match.tick(0)

    @staticmethod
    def rotate_left():
        GameServer.match.try_rotate(0)
        GameServer.match.tick(0)

    @staticmethod
    def get_board():
        return GameServer.match.get_board()
