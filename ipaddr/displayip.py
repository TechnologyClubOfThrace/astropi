#!/usr/bin/python
from sense_hat import SenseHat
import socket
import fcntl
import struct

def get_interface_ipaddress(network):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', network[:15])
        )[20:24])
    except:
        return ""


sense = SenseHat()
sense.set_rotation(270)

red = (255, 0, 0)

i=0
while i<2:
   wlanip = get_interface_ipaddress('wlan0')
   lanip = get_interface_ipaddress('eth0')

   ipaddr = "Lan:  " + lanip + "  Wifi: " + wlanip

   print (ipaddr)

   sense.show_message(ipaddr, text_colour=red, scroll_speed=0.06)
   i=i+1


