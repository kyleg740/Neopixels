import board
import random
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.5)

red = [255, 0, 0]
orange = [255, 64, 0]
yellow = [255, 100, 0]
green = [36, 179, 0]
blue = [15, 139, 212]
purple = [229, 2, 245]
pink = [247, 126, 169]
white = (255, 255, 255)
black = [0, 0, 0]
colors = [red, orange, yellow, green, blue, purple, white, black]


num = 0

def Wipe(color, speed):
    for i in range(np.n):
        np[i] = color
        np.show()
        time.sleep(speed)
    
def Reverse_Wipe(color, speed):
    for i in range(np.n - 1, -1, -1):
        np[i] = color
        np.show()
        time.sleep(speed)
        
def Pattern(color, speed):
    for i in range(np.n):
        np[i] = color[i % len(color)]
        np.show()
        time.sleep(speed)
        
def Reverse_Pattern(color, speed):
    for i in range(np.n - 1, -1, -1):
        np[i] = color[i % len(color)]
        np.show()
        time.sleep(speed)        

while True:
    Wipe(red, 0.1)
    Reverse_Wipe(blue, 0.1)
    Pattern(colors, 0.1)
    Reverse_Pattern(blue, 0.1)
