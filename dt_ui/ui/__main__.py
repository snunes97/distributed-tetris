from stubs import PORT_REQREP, PORT_PUBSUB, HOST, GameServer
from ui.client import Client

game_server = GameServer(HOST, PORT_REQREP, PORT_PUBSUB)
client = Client(game_server)
client.try_enter()
