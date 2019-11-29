from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

b = (0, 0, 0)
y = (248, 252, 0)
r = (255, 0, 0)
           
smiley_face = [b, b, y, y, y, y, b, b, 
               b, y, b, b, b, b, y, b, 
               y, b, y, b, b, y, b, y, 
               y, b, b, b, b, b, b, y, 
               y, b, y, b, b, y, b, y, 
               y, b, b, y, y, b, b, y, 
               b, y, b, b, b, b, y, b, 
               b, b, y, y, y, y, b, b
		        ]

frowning_face = [b, b, y, y, y, y, b, b, 
                 b, y, b, b, b, b, y, b, 
                 y, b, r, b, b, r, b, y, 
                 y, b, b, b, b, b, b, y, 
                 y, b, b, r, r, b, b, y, 
                 y, b, r, b, b, r, b, y, 
                 b, y, b, b, b, b, y, b, 
                 b, b, y, y, y, y, b, b
		          ]

while True:
    sense.set_pixels(smiley_face)
    sleep(2)
    sense.set_pixels(frowning_face)
    sleep(2)

