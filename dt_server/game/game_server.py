from game.player import Player
from game.match import Match


class GameServer:
    match = None
    player_list = []

    @staticmethod
    def validate_player(name: str):
        for player in GameServer.player_list:
            if name == player.name:
                return False

        new_player = Player(name)
        GameServer.player_list.append(new_player)
        match1 = Match(new_player)
        GameServer.match = match1
        GameServer.match.place_new_piece()
        GameServer.match.print_board()
        return True

    @staticmethod
    def move_right():
        GameServer.match.try_move_right()
        GameServer.match.tick()

    @staticmethod
    def move_left():
        GameServer.match.try_move_left()
        GameServer.match.tick()

    @staticmethod
    def rotate_right():
        GameServer.match.try_rotate(1)
        GameServer.match.tick()

    @staticmethod
    def rotate_left():
        GameServer.match.try_rotate(0)
        GameServer.match.tick()

    @staticmethod
    def get_board():
        return GameServer.match.get_board()
