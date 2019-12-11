#!/usr/bin/python

# INSTALL WITH
# sudo apt install python3-gpiozero
import RPi.GPIO as GPIO
from random import uniform
import time
from gpiozero import LED, Button

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #left
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #right

GPIO.setup(22, GPIO.OUT) #BLUE
GPIO.setup(23, GPIO.OUT) #RED
GPIO.setup(24, GPIO.OUT) #GREEN

ledR = LED(22)
ledG = LED(23)
ledB = LED(24)

buttonR = Button(17)
buttonL = Button(18)

def turn_led_on(led):
  if led & 1 == 1:
      ledR.on()
  elif led & 2 == 2:
      ledG.on()
  elif led & 4 == 4:
      ledB.on()

def turn_led_off(led):
  if led & 1 == 1:
      ledR.off()
  elif led & 2 == 2:
      ledG.off()
  elif led & 4 == 3:
      ledB.off()

def redOn():
    turn_led_on(1)

def greenOn():
    ledG.on()

def blueOn():
    ledB.on()

def yellowOn():
    ledR.on()
    ledG.on()

def cyanOn():
    ledG.on()
    ledB.on()

def magentaOn():
    ledR.on()
    ledB.on()

def whiteOn():
    ledR.on()
    ledG.on()
    ledB.on()

def turnAllOff():
    ledR.off()
    ledG.off()
    ledB.off()

def flashR():
  for x in range(1,5):
    redOn()
    time.sleep(0.2)
    turnAllOff()
    time.sleep(0.2)

def rotateRGB():
  for x in range(1,5):
    redOn()
    time.sleep(0.2)
    turnAllOff()
    greenOn()
    time.sleep(0.2)
    turnAllOff()
    blueOn()
    time.sleep(0.2)
    turnAllOff()
    time.sleep(0.2)


GameOn = True
AllowPress = False

def button_pressed(button):
    global AllowPress
    global GameOn

    print ("Button pressed")

    if AllowPress:
      if button == buttonL:
         AllowPress = False
         GameOn = False
         print ('LEFT won the game')
         yellowOn()
      else:
         AllowPress = False
         GameOn = False
         print ('RIGHT won the game')
         magentaOn()
    elif GameOn:
        print ('Too early pressed')
        flashR()

buttonL.when_pressed = button_pressed
buttonR.when_pressed = button_pressed


while GameOn:
   rotateRGB()

   time.sleep(0.5)
   whiteOn()
   time.sleep(uniform(2,5))
   AllowPress = True
   turnAllOff()

   time.sleep(3)
   AllowPress = False

   time.sleep(2)
   GameOn = True



