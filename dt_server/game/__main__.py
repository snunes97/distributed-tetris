import skeletons
import game


def main():
    server = skeletons.GameServer(game.HOST, game.PORT_REQREP, game.PORT_PUBSUB, game.GameServer())
    server.run()


main()
