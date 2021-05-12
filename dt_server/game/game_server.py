from game.player import Player


class GameServer:
    player1 = Player("Marin")
    player_list = [player1]

    @staticmethod
    def validate_player(name: str):
        for player in GameServer.player_list:
            if name == player.name:
                return False
        new_player = Player(name)
        GameServer.player_list.append(new_player)
        return True
