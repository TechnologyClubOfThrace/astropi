#!/usr/bin/python
from sense_hat import SenseHat
import socket
import fcntl
import struct

def get_interface_ipaddress(network):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', network[:15])
    )[20:24])


sense = SenseHat()
sense.set_rotation(270)

red = (255, 0, 0)

i=0
while i<2:
   sense.show_message("My IP:" + get_interface_ipaddress('wlan0'), text_colour=red, scroll_speed=0.06)
   i=i+1


