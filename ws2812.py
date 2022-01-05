import board
import neopixel
pixelCount = 30
pixels = neopixel.NeoPixel(board.D18, pixelCount)
pixels[0] = (255, 0, 0)
for i in range(pixelCount - 2):
	pixels[i + 1] = (0, 255, 0)
pixels[pixelCount - 1] = (0, 0, 255)