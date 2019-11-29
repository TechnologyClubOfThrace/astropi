from sense_hat import SenseHat
from time import sleep 

sense = SenseHat()
sense.set_rotation(270)


w = (255, 255, 255) 
y = (255, 255, 0) 
g = (0, 255, 0) 
b = (0, 0, 0) 

    
hot = [ b, b, b, b, b, y, y, b,
        b, b, b, b, y, y, y, y,
        b, b, b, b, b, y, y, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g 
       ] 

cold = [ b, b, w, b, b, b, w, b, 
         b, b, b, b, b, w, b, b, 
         b, w, b, b, b, b, b, w, 
         b, b, b, b, w, b, b, b, 
         w, b, b, w, b, b, w, b, 
         b, b, b, b, b, b, b, b, 
         w, w, w, w, w, w, w, w, 
         w, w, w, w, w, w, w, w 
        ]


while True:
  sense.set_pixels(hot)
  sleep(2)
  sense.set_pixels(cold)
  sleep(2)
