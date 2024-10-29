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
    """
    Has a background color and randomly flashes a foreground individual pixel.

    Args:
        number[int] = sets the random number
        foreground[tuple] = sets the foreground color
        background[tuple] = sets the background color
        delay[double] = sets the delay

    Returns:
        a + b
    """
    return a + b
    np.fill(background)
    np.show()
    for i in range(random.randint(1, 3)):
        num = random.randint(0, 29)
        np[num] = foreground
        np.show()
        time.sleep(delay)
        
def chase():
    """
    2 pixels chase each other.

    Args:
        count[int] = zero

    Returns:
        The pixels chase each other
    """
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
    """
    Whole strip randomly flashes.

    Args:
        color[tuple] = sets the background color

    Returns:
        The light flashes.
    """
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
    """
    Strips lights flicker.

    Args:
        num[int] = sets a number
        prim_color = sets the background color
        sec_color1 = set a color
        sec_color2 = set a second color

    Returns:
        The leds flicker 2 colors.
    """
    for i in range (num):
        sparkle(sec_color1, prim_color, 0.1, 0.1)
        sparkle(sec_color2, sec_color1, 0.2, 0.1)
   
def fade_in(color, speed):
    """
    Strips lights fade in.

    Args:
        color = set a color
        speed = how quicky it fades

    Returns:
        The leds fade in.
    """
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
    """
    Strips lights fade out.

    Args:
        color = set a color
        speed = how quicky it fades

    Returns:
        The leds fade out.
    """
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
    fire(5, green, yellow, orange)
    chase()
    sparkle(orange, purple, 0.1, 6)
    lightning(purple)
    fade_in(orange, 0.1)
    fade_out(orange, 0.1)
