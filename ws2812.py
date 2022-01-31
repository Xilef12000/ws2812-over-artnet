import board
import neopixel

import json
data = json.load(open('C:\\Users\\Manuel\\Documents\\GitHub\\ws2812-over-artnet\\config.json'))
universe = data["universe"]
pixelCount = data["pixels"]

#pixelCount = 30
pixels = neopixel.NeoPixel(board.D18, pixelCount)
pixels[0] = (255, 0, 0)
for i in range(pixelCount - 2):
	pixels[i + 1] = (0, 255, 0)
pixels[pixelCount - 1] = (0, 0, 255)