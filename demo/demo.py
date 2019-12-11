#!/usr/bin/python
import time
from sense_hat import SenseHat
from random import randint

sense = SenseHat()
sense.set_rotation(270)

r = 255
g = 0
b = 0

msleep = lambda x: time.sleep(x / 1000.0)


pixels = [
    [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
    [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
    [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
    [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
    [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
    [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
    [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
    [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
]

################

def next_colour():
    global r
    global g
    global b

    if (r == 255 and g < 255 and b == 0):
        g += 1

    if (g == 255 and r > 0 and b == 0):
        r -= 1

    if (g == 255 and b < 255 and r == 0):
        b += 1

    if (b == 255 and g > 0 and r == 0):
        g -= 1

    if (b == 255 and r < 255 and g == 0):
        r += 1

    if (r == 255 and b > 0 and g == 0):
        b -= 1

def colour_cycle():
   for x in range (1, 255):
    sense.clear([r, g, b])
    msleep(2)
    next_colour()


####################

def next_pixel_colour(pix):
    r = pix[0]
    g = pix[1]
    b = pix[2]

    if (r == 255 and g < 255 and b == 0):
        g += 1

    if (g == 255 and r > 0 and b == 0):
        r -= 1

    if (g == 255 and b < 255 and r == 0):
        b += 1

    if (b == 255 and g > 0 and r == 0):
        g -= 1

    if (b == 255 and r < 255 and g == 0):
        r += 1

    if (r == 255 and b > 0 and g == 0):
        b -= 1

    pix[0] = r
    pix[1] = g
    pix[2] = b



def rainbow():
  for x in range (1, 10):
    for pix in pixels:
        next_pixel_colour(pix)

    sense.set_pixels(pixels)
    msleep(2)
  time.sleep(1)

####################

def random_sparkles():

  for k in range (1, 255):
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
    time.sleep(0.01)


def rotate_text():
   r = randint(0, 255)
   g = randint(0, 255)
   b = randint(0, 255)

   col = (r, g, b)

   sense.show_message("Welcome to Hour of Code by STETH", 
             text_colour=col, scroll_speed=0.05)


def display_temp():
  r = (255, 0, 0)
  temp = round( sense.temperature, 1 )

  sense.show_message( "Temp " + str(temp) + " C",
               scroll_speed=0.05, text_colour=r)

def display_humidity():
  g = (0, 255, 0)
  humidity = round( sense.get_humidity(), 1 )

  sense.show_message( "Humidity " + str(humidity) + " %",
               scroll_speed=0.05, text_colour=g)


while True:
   colour_cycle()
   rainbow()
   random_sparkles()
   rotate_text()
   time.sleep(1)
   display_temp()
   time.sleep(1)
   display_humidity()
   time.sleep(1)

