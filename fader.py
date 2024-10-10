import board
import time
import random
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=1)
red = (255, 0, 0)
orange = (255, 136, 0)
yellow = (255, 242, 0)
green = (36, 179, 0)
blue = (0, 0, 255)
purple = (162, 45, 224)
pink = (247, 126, 169)
white = (255, 255, 255)

colors = [red, orange, yellow, green, blue, purple, white]

def fade_in(color, speed):
    red_original = color[0]
    green_original = color[1]
    blue_original = color[2]
    red_ratio = color[0] / 50
    green_ratio = color[1] / 50
    blue_ratio = color[2] / 50
    for i in range(1, 51):
        A = red_original + i * red_ratio
        B = green_original + i * green_ratio
        C = blue_original + i * blue_ratio
        np.fill((A, B, C))
        np.show()
        time.sleep(speed)

def fade_out(color, speed):
    red_original = color[0]
    green_original = color[1]
    blue_original = color[2]
    red_ratio = color[0] / 50
    green_ratio = color[1] / 50
    blue_ratio = color[2] / 50
    for i in range(1, 51):
        A = red_original - i * red_ratio
        B = green_original - i * green_ratio
        C = blue_original - i * blue_ratio
        np.fill((A, B, C))
        np.show()
        time.sleep(speed)



while True:
    fade_in(red, 0.1)
    fade_out(red, 0.1)
