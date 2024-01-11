import time

def off(strip):
    strip.fill((0,0,0))
    strip.show()

def chase(strip, cl1, cl2, delay, times):
    strip.fill(cl1)
    strip.set_pixel(0,cl2)
    numpix = strip.num_leds
    x = 0
    while x < times:
        while strip.get_pixel(0) != cl2:
            strip.rotate_left(1)
            time.sleep(delay)
            strip.show()
        while strip.get_pixel(numpix-1) != cl2:
            strip.rotate_right(1)
            time.sleep(delay)
            strip.show()
        x += 1

def chase3(strip, cl1, cl2, cl3, delay, times):
    x=0
    y=0
    while x < (strip.num_leds - 2):
        strip.set_pixel(x, cl1)
        strip.set_pixel(x+1, cl2)
        strip.set_pixel(x+2, cl3)
        x += 3
    while y <= times:
        strip.rotate_right(1)
        time.sleep(delay)
        strip.show()
        y += 1

def bars(strip, cl1, cl2, count):
    sections = int(strip.num_leds/count)
    for x in range(sections):
        if x % 2 != 0:
            strip.set_pixel_line(x*count, (x*count)+count, cl1)
        if x % 2 == 0:
            strip.set_pixel_line(x*count, (x*count)+count, cl2)
    strip.show()
    
def bars_shift(strip, cl1, cl2, count, delay, times):
    bars(strip,cl1,cl2,count)
    x=0
    while x <= times:
        strip.rotate_right(1)
        time.sleep(delay)
        strip.show()
        x += 1
