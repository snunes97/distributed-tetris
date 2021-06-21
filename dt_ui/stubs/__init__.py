from stubs.client_stub import ClientStub
#25.67.247.53 - Testes com hamachi (WORKS!)

# Ip dp cliente
HOST = "25.67.247.53"

# Portas dos sockets request-reply e publisher-subscriver
PORT_REQREP = 5001
PORT_PUBSUB = 5002

# Comandos
OP_VALIDATEPLAYER = "VALIDATEPLAYER"
OP_MOVERIGHT = "MOVERIGHT"
OP_MOVELEFT = "MOVELEFT"
OP_ROT_R = "ROTRIGHT"
OP_ROT_L = "ROTLEFT"
OP_GETBOARD = "GETBOARD"
OP_BOARDUPDATE = "UPDATEBOARD"
OP_MATCHEXISTS = "MATCHEXISTS"
OP_DISCONNECT = "DISCONNECT"

# Quando o ClienteStub é criado o init executa o que está neste script.