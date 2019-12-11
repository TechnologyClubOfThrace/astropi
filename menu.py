#!/usr/bin/python
from sense_hat import SenseHat
import os
import time
import RPi.GPIO as GPIO
import subprocess

##### joystick libraries #####
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

homedir = "/home/pi/astropi/"

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 255, 255)
y = (255, 255, 0)

menu = [
  ("Demo",        g, "/usr/bin/python", "demo/demo.py"),
  ("Clock",       b, "/usr/bin/python", "clock/clock.py"),
  ("Colour",      b, "/usr/bin/python", "sensehat/colour_cycle.py"),

  ("Maze",        y, "/usr/bin/python", "marble-maze/marble-maze.py"),
  ("Dice",        g, "/usr/bin/python", "dice/dice.py"),
  ("Ball",        y, "/usr/bin/python", "gravity/gravity_ball.py"),

  ("Rainbow",     b, "/usr/bin/python", "sensehat/rainbow.py"),

  ("Conway",      g, "/usr/bin/python", "sensehat2/conway.py"),
  ("Sparkles",    b, "/usr/bin/python", "sensehat2/random_sparkles.py"),
  ("Temp",        b, "/usr/bin/python", "sensehat2/temperature.py"),
  ("Humidity",    b, "/usr/bin/python", "sensehat2/humidity.py"),

  ("Text",        b, "/usr/bin/python", "sensehat/text_scroll.py"),

#  ("Egg",         g, "/usr/bin/python", "egg/eggdrop.py"),
#  ("Compass",     b, "/usr/bin/python", "examples/compass.py"),

  ("IPAddr",      r, "/usr/bin/python", "ipaddr/displayip.py"),
  ("Poweroff",    r, "poweroff", "")
]

current = 0
current_proc =  None

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) #UP
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #DOWN
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) #LEFT
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) #RIGHT
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #2LEFT
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #2RIGHT

last_LR = 0

def go_up():
    global current
    global last_LR
    last_LR = 0
    current = current-1
    if current<0:
        current = len(menu)-1
    print_menu(current)

def go_down():
    global current
    global last_LR
    last_LR = 0
    current=current+1
    if current>len(menu)-1:
        current = 0
    print_menu(current)

def go_left():
    global last_LR
    last_LR = 1

def go_right():
    global last_LR
    if last_LR == 2:
        stop_process()
        last_LR = 0
    else:
        last_LR = 2

def go_click():
    global current
    run_process(current)


def pushed_down(event):
    if event.action != ACTION_RELEASED:
        print ("Joystick DOWN")
        go_down()

def pushed_up(event):
    if event.action != ACTION_RELEASED:
        print ("Joystick UP")
        go_up()

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        print ("Joystick LEFT")
        go_left()

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        print ("Joystick RIGHT")
        go_right()

def pushed_click(event):
    if event.action != ACTION_RELEASED:
        print ("Joystick CLICK")
        go_click()

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


#############  Start of main program
time.sleep(1)

sense = SenseHat()
sense.clear()  # Blank the LED matrix
sense.set_rotation(270)  # Flight orientation

##### Make Joystick Available #####
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_click


running = True

print_menu(current)


while running:
    if GPIO.input(26) == 0:
        print ("button 26 - UP")
        go_up()

    if GPIO.input(13) == 0:
        print ("button 13 - DOWN")
        go_down()

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
