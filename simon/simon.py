#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
import random
from gpiozero import LED, Button

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) #YELLOW
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) #BLUE
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #RED
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) #GREEN

GPIO.setup(18, GPIO.OUT) #YELLOW
GPIO.setup(24, GPIO.OUT) #BLUE
GPIO.setup(12, GPIO.OUT) #RED
GPIO.setup(21, GPIO.OUT) #GREEN

led1 = LED(18)
led2 = LED(24)
led3 = LED(12)
led4 = LED(21)

button1 = Button(22)
button2 = Button(4)
button3 = Button(13)
button4 = Button(27)


target_seq = []
global user_seq

user_seq = []
user_seq = []
leds_list = [1,2,3,4]


def turn_led_on(led):
#  print("Led on" + str(led))

  if led == 1:
      led1.on()
  elif led == 2:
      led2.on()
  elif led == 3:
      led3.on()
  else:
      led4.on()

def turn_led_off(led):
#  print("Led off" + str(led))

  if led == 1:
      led1.off()
  elif led == 2:
      led2.off()
  elif led == 3:
      led3.off()
  else:
      led4.off()

def button_pressed(b):
   if b == button1:
       led=1
   elif b == button2:
       led=2
   elif b == button3:
       led=3
   else:
       led=4

   turn_led_on(led)

def button_released(b):
   if b == button1:
       led=1
   elif b == button2:
       led=2
   elif b == button3:
       led=3
   else:
       led=4

   turn_led_off(led)
   user_seq.append(led)


def led_on_off():
    for x in range(1,5):
     turn_led_on(x)

    time.sleep(0.5)

    for x in range(1,5):
     turn_led_off(x)

    time.sleep(0.5)

def turn_all_on_off():
    for x in range(1,5):
     turn_led_on(x)

    time.sleep(0.5)

    for x in range(1,5):
     turn_led_off(x)

def rotate_all_on_off():

  for y in range (1,4):
    for x in range(1,5):
        turn_led_on(x)
        time.sleep(0.1)
        turn_led_off(x)

    time.sleep(0.1)

  time.sleep(0.3)

  for y in range (1,4):
    for x in range(4,0, -1):
        turn_led_on(x)
        time.sleep(0.1)
        turn_led_off(x)

    time.sleep(0.1)

  time.sleep(1)


button1.when_pressed = button_pressed
button2.when_pressed = button_pressed
button3.when_pressed = button_pressed
button4.when_pressed = button_pressed

button1.when_released = button_released
button2.when_released = button_released
button3.when_released = button_released
button4.when_released = button_released


print ('Starting. Copy the sequence.')
level = 0
GameOn = True
gap = 0.8

rotate_all_on_off()

while GameOn:
 user_seq = []

 level+=1
 count = 1
 print ('Starting Level ' + str(level))

 for i in  range(count):
  led = random.choice(leds_list)
  target_seq.append(led)

 print ("target seq", target_seq)

 for seq_n in target_seq:
  turn_led_on(seq_n)
  time.sleep(gap)
  turn_led_off(seq_n)
  time.sleep(gap)

 countdown = 20
 waiting = True

 while waiting:

  if (len(user_seq) == len(target_seq)) or (countdown == 0):
   if user_seq == target_seq:
    waiting = False

    print (user_seq, target_seq)
    time.sleep(0.5)

    print ('Correct')
    turn_all_on_off()

    gap = gap* 0.8

   else:
    waiting = False

    GameOn = False
    print ('Fail')
    print ('You reached level:' + str(level) )

    time.sleep(2)
    print("Starting Over")
    rotate_all_on_off()
    target_seq = []
    level = 0
    GameOn = True

  time.sleep(1)
  countdown-=1

 time.sleep(2)


