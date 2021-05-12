import skeletons
import game


def main():
    server = skeletons.GameServer(game.HOST, game.PORT, game.GameServer())
    server.run()


main()
