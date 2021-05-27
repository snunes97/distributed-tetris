from game.player import Player
from game.match import Match


class Server:
    match = None
    min_players = 1
    player_list = []

    @staticmethod
    def start_new_match(player1):
        match1 = Match(player1, Server)
        Server.match = match1
        Server.match.place_new_piece()
        Server.match.print_board()
        Server.match.start_timer()

    @staticmethod
    def validate_player(name: str):
        for player in Server.player_list:
            if name == player.name:
                return False

        new_player = Player(name)
        Server.player_list.append(new_player)
        return True

    @staticmethod
    def check_game_start():
        if len(Server.player_list) == Server.min_players:
            Server.start_new_match(Server.player_list[0])
            return True
        return False

    @staticmethod
    def move_right():
        Server.match.try_move_right()
        Server.match.tick(0)

    @staticmethod
    def move_left():
        Server.match.try_move_left()
        Server.match.tick(0)

    @staticmethod
    def rotate_right():
        Server.match.try_rotate(1)
        Server.match.tick(0)

    @staticmethod
    def rotate_left():
        Server.match.try_rotate(0)
        Server.match.tick(0)

    @staticmethod
    def get_board():
        return Server.match.get_board()

    @staticmethod
    def match_exists():
        # print("match exists: " + str(GameServer.match is not None))
        return Server.match is not None