#!/usr/bin/python
from sense_hat import SenseHat
import math
import time
sense = SenseHat()
r = 128
g = 128
b = 128
old_x = 0
old_y = 0
def draw(x,y):
    global old_x, old_y, r, g, b
    sense.set_pixel(x, y, r, g, b)
    if old_x != x or old_y != y:
        sense.set_pixel(old_x, old_y, 0, 0, 0)
    old_x = x;
    old_y = y;
def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))
def next(v,gv):
    if gv < -0.12:
        return v - 1
    elif gv > 0.12:
        return v + 1
    else:
        return v
def pushed_up():
    global r, g, b
#    r = clamp(r - 2, 0, 255)
    g = clamp(g + 4, 0, 255)
#    b = clamp(b - 2, 0, 255)
def pushed_left():
    global r, g, b
    r = clamp(r + 4, 0, 255)
#    g = clamp(g - 2, 0, 255)
#    b = clamp(b - 2, 0, 255)
def pushed_right():
    global r, g, b
#    r = clamp(r - 2, 0, 255)
#    g = clamp(g - 2, 0, 255)
    b = clamp(b + 4, 0, 255)
def pushed_down():
    global r, g, b
    g = clamp(g - 4, 0, 255)
    r = clamp(r - 4, 0, 255)
    b = clamp(b - 4, 0, 255)
def pushed_middle():
    global r, g, b
    g = 128
    r = 128
    b = 128
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
sense.clear()
x = 3
y = 3
draw(x, y)
while True:
    accel = sense.get_accelerometer_raw()
    gx, gy = accel['x'], accel['y']
    mag = math.sqrt(gx * gx + gy * gy)
    x = clamp(next(x, gx))
    y = clamp(next(y, gy));
    draw(x, y)
    mag = math.sqrt(gx * gx + gy * gy)
    amount = mag / .6
    adjust = .1 * amount
    time.sleep(clamp(.15 - adjust, .01, .15))

