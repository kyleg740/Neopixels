import board
import random
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=1)
red = [255, 0, 0]
orange = [255, 136, 0]
yellow = [255, 242, 0]
green = [36, 179, 0]
blue = [15, 139, 212]
purple = [162, 45, 224]
pink = [247, 126, 169]
white = [255, 255, 255]

colors = [red, orange, yellow, green, blue, purple, white]


def sparkle (background, foreground, delay, number):
    np.fill(background)
    np.show()
    for i in range(number):
        num = random.randint(0, 29)
        np[num] = foreground
        np.show()
        time.sleep(delay)

while True:
    sparkle(green, white, 0.01, 5)
