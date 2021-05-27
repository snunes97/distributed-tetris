import skeletons
import game


def main():
    skeleton = skeletons.ServerSkeleton(skeletons.HOST, skeletons.PORT_REQREP, skeletons.PORT_PUBSUB, game.Server())
    game.Server().set_skeleton(skeleton)
    skeleton.run()


main()
