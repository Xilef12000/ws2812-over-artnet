from stupidArtnet import StupidArtnetServer

import json
data = json.load(open('C:\\Users\\Manuel\\Documents\\GitHub\\ws2812-over-artnet\\config.json'))
universe = data["universe"]

def test_callback(data):
	print(data)

#universe = 1
server = StupidArtnetServer()
u1_listener = server.register_listener(universe, callback_function=test_callback)
input("stop?")
del server