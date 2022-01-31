import time
import board
import neopixel
from stupidArtnet import StupidArtnetServer
import json
import os

dirname = os.path.dirname(__file__)
data = json.load(open(os.path.join(dirname, 'config.json')))
universe = data["universe"]
pixelCount = data["pixels"]

#pixelCount = 30
pixels = neopixel.NeoPixel(board.D18, pixelCount)

#universe = 1
server = StupidArtnetServer()
u1_listener = server.register_listener(universe)
while True:
	data = server.get_buffer(listener_id=u1_listener)
	if len(data) > 0:
		#print(data)
		for i in range(pixelCount):
			pixels[i] = (data[(3 * i) + 0], data[(3 * i) + 1], data[(3 * i) + 2])
del server
