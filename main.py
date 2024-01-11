import time
from neopixel import Neopixel
import lightfunc as lf

numpix = 50
s0 = Neopixel(numpix, 0, 28, "RGB")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255,255,255)
s0.brightness(75)

def main():
    lf.chase(s0, green, red, 0.1, 2)
    time.sleep(0.2)
    lf.chase3(s0, red, green, white, 0.4, 20)
    time.sleep(0.2)
    lf.off(s0)
    time.sleep(0.2)
    lf.bars_shift(s0,red,blue,5,0.2,60)
    time.sleep(0.2)
    lf.off(s0)

if __name__ == "__main__":
    main()

