import board
import neopixel
import json
import os

dirname = os.path.dirname(__file__)
data = json.load(open(os.path.join(dirname, 'config.json')))
pixelCount = data["pixels"]

#pixelCount = 30
pixels = neopixel.NeoPixel(board.D18, pixelCount)
pixels[0] = (255, 0, 0)
for i in range(pixelCount - 2):
	pixels[i + 1] = (0, 255, 0)
pixels[pixelCount - 1] = (0, 0, 255)