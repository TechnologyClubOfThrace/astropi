from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.set_rotation(270)

r = (255, 0, 0)
b = (0, 0, 255)

sense.set_pixel(0, 2, b)
sense.set_pixel(7, 4, r)

