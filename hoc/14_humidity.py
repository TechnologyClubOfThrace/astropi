from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)



while True:
    humidity = round( sense.get_humidity(), 1 ) 

    sense.show_message( str(humidity) +"%" ) 
    #sense.show_message("Humidity is: " + str(humidity) + "%" ) 


