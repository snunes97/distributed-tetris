from stubs import PORT, HOST, GameServer

newName = input("Insert your player name: ")
game_server = GameServer(HOST, PORT)

game_server.validate_player(newName)
