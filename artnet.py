from stupidArtnet import StupidArtnetServer
import json
import os

dirname = os.path.dirname(__file__)
data = json.load(open(os.path.join(dirname, 'config.json')))
universe = data["universe"]

def test_callback(data):
	print(data)

#universe = 1
server = StupidArtnetServer()
u1_listener = server.register_listener(universe, callback_function=test_callback)
input("stop?")
del server