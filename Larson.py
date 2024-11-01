import board
import random
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.5)
red = [255, 0, 0]
orange = [255, 64, 0]
yellow = [255, 100, 0]
green = (36, 179, 0)
blue = [15, 139, 212]
purple = [229, 2, 245]
pink = [247, 126, 169]
white = (255, 255, 255)
black = [0, 0, 0]

colors = [red, orange, yellow, green, blue, purple, white, black]


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
 
def canner(foreground, background, bounce_num = 2):
    num = 0
    one = 1
    bounce = 0
    new_color = [int(c * 0.8) for c in foreground]
    while num < bounce_num: 
        np.fill(background)
        np[num] = foreground
        np[num + 1] = foreground
        np[num - 1] = foreground
        time.sleep(0.1)
        np.show()
        num += one
        if (bounce >= (np.n - 1) or bounce == 0):
            one *= -1
            bounce += 1
        if ((num - 1) <= np.n - 1):
            np[(num - 1) % np.n] = foreground
            
            
        
        np.show()
        
               
while True:
    canner(green, black)
