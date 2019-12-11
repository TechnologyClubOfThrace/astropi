from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)

w = (255, 255, 255) 
b = (0, 0, 0)

picture = [ b, b, w, w, w, w, b, b, 
            b, w, b, b, b, b, w, b, 
            b, w, b, w, w, b, w, b, 
            b, w, b, b, b, b, w, b, 
            b, b, w, w, w, w, b, b, 
            b, b, w, w, w, w, b, b, 
            b, w, w, w, w, w, w, b, 
            b, w, w, w, w, w, w, b 
           ] 

sense.set_pixels(picture)

