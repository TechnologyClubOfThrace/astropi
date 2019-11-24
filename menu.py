#!/usr/bin/python
from sense_hat import SenseHat
import os
import time
import RPi.GPIO as GPIO
import subprocess

homedir = "/home/pi/senseHat/"

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 255, 255)
y = (255, 255, 0)

menu = [
  ("Clock",       b, "/usr/bin/python", "clock.py"),
  ("Text",        b, "/usr/bin/python", "examples/text_scroll.py"),
  ("Colour",      b, "/usr/bin/python", "examples/colour_cycle.py"),
#  ("Match Color", b, "/usr/bin/python", "examples/colour_match.py"),
  ("Conway",      g, "/usr/bin/python", "examples/conway.py"),
  ("Dice",        g, "/usr/bin/python", "dice.py"),
  ("Ball",        y, "/usr/bin/python", "gravity_ball.py"),
  ("Maze",        y, "/usr/bin/python", "marble-maze.py"),
  ("Sparkles",    b, "/usr/bin/python", "examples/random_sparkles.py"),
  ("Rainbow",     b, "/usr/bin/python", "examples/rainbow.py"),
#  ("Egg",         g, "/usr/bin/python", "egg/eggdrop.py"),
  ("Compass",     b, "/usr/bin/python", "examples/compass.py"),
  ("Temp",        b, "/usr/bin/python", "examples/temperature.py"),
  ("Humidity",    b, "/usr/bin/python", "examples/humidity.py"),
  ("IPAddr",      r, "/usr/bin/python", "ipaddr/displayip.py"),
  ("Poweroff",    r, "poweroff", "")
]

current_proc =  None

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) #UP
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #DOWN
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) #LEFT
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) #RIGHT
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #2LEFT
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #2RIGHT

time.sleep(1)

sense = SenseHat()
sense.clear()  # Blank the LED matrix
sense.set_rotation(270)  # Flight orientation

def print_menu(choice):
    sense.show_message(menu[choice][0], scroll_speed=0.05, text_colour=menu[choice][1])


def run_process(choice):
    global current_proc
    if (current_proc != None):
       current_proc.kill()

    cmdline = menu[choice][3]
    if cmdline != "":
        cmdline = homedir + cmdline

    print "executing " + menu[choice][2] + " " + cmdline

    if (choice == len(menu) -1):
        current_proc = subprocess.Popen( "poweroff" )
    else:
        current_proc = subprocess.Popen( [menu[choice][2], cmdline])

    print current_proc

def stop_process():
    global current_proc

    if (current_proc != None):
       print "killing process"
       print current_proc
       current_proc.kill()
    current_proc = None

    print_menu(current)

running = True

current = 0
print_menu(current)


while running:
    if GPIO.input(26) == 0:
        print ("button 26 - UP")
        current = current-1
        if current<0:
            current = len(menu)-1
        print_menu(current)

    if GPIO.input(13) == 0:
        print ("button 13 - DOWN")
        current=current+1
        if current>len(menu)-1:
            current = 0
        print_menu(current)

    if GPIO.input(19) == 0:
        print ("button 19")

    if GPIO.input(20) == 0:
        print ("button 20")

    if GPIO.input(16) == 0:
        print ("button 16 - right click")
        stop_process()

    if GPIO.input(21) == 0:
        print ("button 21 - left click")
        run_process(current)

    time.sleep(0.2)
