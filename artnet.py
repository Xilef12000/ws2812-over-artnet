from stupidArtnet import StupidArtnetServer

def test_callback(data):
	print(data)

universe = 1
server = StupidArtnetServer()
u1_listener = server.register_listener(universe, callback_function=test_callback)
input("stop?")
del server