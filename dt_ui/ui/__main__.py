from stubs import PORT, HOST, GameServer
from ui.client import Client

game_server = GameServer(HOST, PORT)
client = Client(game_server)
client.try_enter()
