from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)

while True:
	sense.show_message("Astro Pi",
    		text_colour=(255, 0, 0),
    		back_colour=(0, 255, 0))

