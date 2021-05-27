from stubs import PORT_REQREP, PORT_PUBSUB, HOST, ClientStub
from ui.client import Client

game_server = ClientStub(HOST, PORT_REQREP, PORT_PUBSUB)
client = Client(game_server)
client.try_enter()
