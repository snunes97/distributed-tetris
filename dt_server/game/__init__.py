from game_server import GameServer
from player import Player

PORT = 5001
HOST = "127.0.0.1"

OP_VALIDATEPLAYER = "VALIDATEPLAYER"
OP_MOVERIGHT = "MOVERIGHT"
OP_MOVELEFT = "MOVELEFT"
OP_ROT_R = "ROTRIGHT"
OP_ROT_L = "ROTLEFT"
OP_GETBOARD = "GETBOARD"
OP_BOARDUPDATE = "UPDATEBOARD"