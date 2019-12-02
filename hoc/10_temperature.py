from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)

while True:
	#temp = sense.temperature

	temp = round( sense.temperature, 1 )

	sense.show_message( str(temp))

	#sense.show_message("It is " + str(temp) + " degrees" )

