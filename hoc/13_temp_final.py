from sense_hat import SenseHat
from time import sleep 

sense = SenseHat()
sense.set_rotation(270)

w = (255, 255, 255) 
y = (255, 255, 0) 
g = (0, 255, 0) 
b = (0, 0, 0) 
r = (255, 0, 0)
bl = (0, 0, 255)


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

sense.show_message("Hello from Alexandroupolis Greece", 
    scroll_speed = 0.05, text_colour=r, back_colour=b)
sleep(1)

while True:
  temp = round( sense.temperature, 1 )

  if temp >= 20: 
      sense.show_message( "Warm " + str(temp) + " C", 
               scroll_speed=0.05, text_colour=r)
      sleep(1)
      sense.set_pixels(hot) 
  else: 
      sense.show_message( "Cold " + str(temp) + " C", 
                scroll_speed=0.05, text_colour=bl)
      sleep(1)
      sense.set_pixels(cold)
      
  sleep(2)
