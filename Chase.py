import board
import random
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.1)
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
        
def chase():
    count = 0
    for i in range(np.n):
        np.fill(orange)
        for i in range(np.n):
            if (i + count) % 3 == 0:
                np[i] = (0, 0, 0)
        time.sleep(0.3)
        np.show()
        count = (count + 1) % 3 
        
def lightning(color):
    np.fill((color))
    np.show()
    
   
while True:
    chase()
    
