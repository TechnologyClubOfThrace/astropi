from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)


while True:
    pressure = round (sense.get_pressure(), 1)

    sense.show_message( str(pressure) )

    #sense.show_message("pressure is: " + str(pressure) + "Millibars" )

