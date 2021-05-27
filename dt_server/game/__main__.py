import skeletons
import game


def main():
    server = skeletons.ServerSkeleton(skeletons.HOST, skeletons.PORT_REQREP, skeletons.PORT_PUBSUB, game.Server())
    server.run()


main()
