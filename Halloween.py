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
white = [255, 255, 255]

colors = [red, orange, yellow, green, blue, purple, white]


def sparkle (background, foreground, delay, number):
    np.fill(background)
    np.show()
    for i in range(random.randint(1, 3)):
        num = random.randint(0, 29)
        np[num] = foreground
        np.show()
        time.sleep(delay)
        
def chase():
    count = 0
    for i in range(np.n):
        np.fill(green)
        for i in range(np.n):
            if (i + count) % 3 == 0:
                np[i] = (0, 0, 0)
        time.sleep(0.1)
        np.show()
        count = (count + 1) % 3 
        
def lightning(color):
    np.fill((color))
    np.show()
    time.sleep(3)
    for i in range(5):
        sleep = random.randint(1,4) / 50
        np.fill((purple))
        np.show()
        time.sleep(sleep)
        np.fill((white))
        np.show()
        time.sleep(sleep)
        
def fire(num, prim_color, sec_color1, sec_color2):
    for i in range (num):
        sparkle(sec_color1, prim_color, 0.1, 0.1)
        sparkle(sec_color2, sec_color1, 0.2, 0.1)
   
while True:
    fire(5, green, yellow, orange)
    chase()
    sparkle(orange, purple, 0.1, 6)
    lightning(purple)
    
