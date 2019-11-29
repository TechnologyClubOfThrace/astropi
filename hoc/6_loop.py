from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)

red = (255,0,0) 
green = (0,255,0) 

while True: 
    sense.show_message("Astro Pi",
                   text_colour=red,
                   back_colour=green)

